import os
from Dataset_Loader import Dataset_Loader
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import json


def cos_sim(dataset):
    numeric = dataset.select_dtypes(
        include=[np.number])
    keys = dataset.select_dtypes(
        exclude=[np.number])
    scaler = StandardScaler()
    scaled = scaler.fit_transform(numeric)
    sims = cosine_similarity(scaled)
    player_mappings = {}
    for i in range(len(keys)):
        analyzed = keys.iloc[i]
        player_sims = sims[i]
        player_df = keys
        player_df['similarity'] = player_sims.tolist()
        sorted_sims = player_df.sort_values(
            by="similarity", axis=0, ascending=False)
        player_mappings[analyzed.player_id] = sorted_sims
    return player_mappings
    # print(analyzed, sorted_sims)
    # input()
    # return sims


if __name__ == "__main__":
    loader = Dataset_Loader(method='file')
    sets = loader.load_all_datasets()
    processed = []
    for dataset in sets:
        data_proc = cos_sim(dataset)
        for player in data_proc.keys():
            similar = data_proc[player].head(
                n=6)
            sim_dict = pd.Series(
                similar.iloc[1:]['similarity'].values, index=similar.iloc[1:]['name']).to_dict()
            sim_dict_proc = {str(k): float(v) for k, v in sim_dict.items()}
            processed.append(
                {'name': str(similar.iloc[0].name), 'similar': sim_dict_proc, 'id': str(player)})

    with open('dataset.json', 'w') as json_file:
        json.dump(processed, json_file)
