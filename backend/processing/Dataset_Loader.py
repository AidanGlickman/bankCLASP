import os
import csv
import pandas as pd
import numpy as np


class Dataset_Loader:
    applicable_path = ""
    players_path = ""
    by_position = {}

    def load_dataset(self, position):
        '''
        returns a dataframe and list of labels for a given position to be used as a dataset
        '''
        position_data = self.by_position[position]
        X_list, y = list(zip(*position_data))
        X = pd.concat(X_list, axis=1).transpose()
        return X, y

    def aggregateStats(self, positionPlayer):
        '''
        sums all the stats to get down to one vector
        '''
        return positionPlayer.sum(axis=0)

    def loadPlayer(self, player_path):
        '''
        loads a player in to the by_position dictionary
        '''
        player_dat = pd.read_csv(player_path)
        # get rid of the career row
        player_dat.drop(player_dat.index[-1], axis=0, inplace=True)
        for pos in player_dat['position'].unique():
            # Kickers and Punters provide errors, and people with no position aren't useful
            if pos in ["P", "K", "PK", "UT", np.nan]:
                continue
            player_pos = player_dat.loc[player_dat['position'] == pos]
            if pos not in self.by_position.keys():
                self.by_position[pos] = []
            # print(pos)
            with open(os.path.join(self.applicable_path, pos + '.csv')) as applicable:
                applicable_stats = list(
                    map(lambda x: x.strip(), applicable.read().split(",")))
                filtered_player = player_pos[applicable_stats]
                self.by_position[pos].append(
                    (self.aggregateStats(filtered_player), player_pos["player_id"].unique()[0]))
        # print(player_dat)

    def loadAllPlayers(self):
        '''
        iterates over all players to add them to by_position
        '''
        for file in os.listdir(self.players_path):
            self.loadPlayer(os.path.join(self.players_path, file, "ncaaf.csv"))

    def __init__(self, applicable_path=os.path.join('applicable'), players_path=os.path.join('pairedPlayers')):
        self.applicable_path = applicable_path
        self.players_path = players_path
        self.loadAllPlayers()


if __name__ == "__main__":
    loader = Dataset_Loader()
    print(loader.load_dataset("QB")[0].info())
