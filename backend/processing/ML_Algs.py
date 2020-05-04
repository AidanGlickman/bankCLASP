import os
from Dataset_Loader import Dataset_Loader
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import numpy as np


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
    dataset = loader.load_dataset("QB")
    cos_sim(dataset)['lamar-jackson-1'].to_csv('jackson.csv')