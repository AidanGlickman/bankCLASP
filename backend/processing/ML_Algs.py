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
        # print(analyzed)
        player_mappings[analyzed['player_id']] = sorted_sims
    return player_mappings
    # print(analyzed, sorted_sims)
    # input()
    # return sims


def nflCosSim():
    loader = Dataset_Loader(method='file')
    sets = loader.load_all_datasets()
    processed = []
    for dataset in sets.keys():
        data_proc = cos_sim(sets[dataset])
        for player in data_proc.keys():
            similar = data_proc[player].head(
                n=6)
            sim_dict = pd.Series(
                similar.iloc[1:]['similarity'].values, index=similar.iloc[1:]['name']).to_dict()
            sim_dict_proc = [{'name': str(k), 'similarity': float(v)}
                             for k, v in sim_dict.items()]
            processed.append(
                {'name': str(similar['name'].tolist()[0]), 'position': dataset, 'similar': sim_dict_proc, 'id': str(player)})

    with open('dataset.json', 'w') as json_file:
        json.dump(processed, json_file)


def procPlayer(player, pos, baseData):
    dataset = baseData[pos]

    dataset = dataset.append(player, sort=False)
    dataset.dropna(how='any', axis='columns', inplace=True)
    # print(dataset.replace([np.inf, -np.inf], np.nan).isna().any())
    # print(player)
    data_proc = cos_sim(dataset)
    playerCos = data_proc[player.player_id.unique()[0]]
    similar = playerCos.head(
        n=6)
    sim_dict = pd.Series(
        similar.iloc[1:]['similarity'].values, index=similar.iloc[1:]['name']).to_dict()
    sim_dict_proc = [{'name': str(k), 'similarity': float(v)}
                     for k, v in sim_dict.items()]
    return {'name': str(player['name'].unique()[0]), 'position': str(pos), 'similar': sim_dict_proc, 'id': str(player.player_id.unique()[0])}


def procNcaaf(ncaaf_path):
    loader = Dataset_Loader(method='file')
    sets = loader.load_all_datasets()
    playerSims = []
    for file in os.listdir(ncaaf_path):
        try:
            player_by_pos = loader.loadPlayer(
                os.path.join(ncaaf_path, file))
            for pos in player_by_pos.keys():
                playerSims.append(procPlayer(player_by_pos[pos], pos, sets))
        except Exception as e:
            print(e)
    with open('dataset.json', 'w') as json_file:
        json.dump(playerSims, json_file)


if __name__ == "__main__":
    procNcaaf(os.path.join('ncaafPlayers'))
    # nflCosSim()
