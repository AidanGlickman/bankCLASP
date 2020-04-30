import os
import csv
import pandas as pd
import numpy as np
import datetime


class Dataset_Loader:
    datasets = {}

    def load_dataset(self, position, drop_unlabeled=True):
        '''
        returns a dataframe for a given position to be used as a dataset
        '''
        position_data = self.by_position[position]
        X = pd.concat(position_data, axis=0)
        X.dropna(axis=0, how='any', inplace=True)
        return X

    def aggregateStats(self, positionPlayer):
        '''
        sums all the stats to get down to one vector
        '''
        non_num = positionPlayer.select_dtypes(exclude=np.number)
        num = positionPlayer.sum(axis=0, numeric_only=True).to_frame().T
        return num.join(non_num)

    def loadPlayer(self, player_path):
        '''
        loads a player and returns a dict giving his aggregated stats by position
        '''
        player_dat = pd.read_csv(player_path)
        # get rid of the career row
        player_dat.drop(player_dat.index[-1], axis=0, inplace=True)
        player_by_pos = {}
        for pos in player_dat['position'].unique():
            # Kickers and Punters provide errors, and people with no position aren't useful
            if pos in ["P", "K", "PK", "UT", np.nan]:
                continue
            player_pos = player_dat.loc[player_dat['position'] == pos]
            filtered_player = player_pos[self.applicables[pos] +
                                         self.applicables['ALL']]
            player_stats = self.aggregateStats(filtered_player)
            # player_stats['id'] = player_pos["player_id"].unique()[0]
            player_by_pos[pos] = player_stats
        return player_by_pos
        # print(player_dat)

    def from_gathered(self, players_path):
        '''
        iterates over all players 
        '''
        by_position = {}
        for file in os.listdir(players_path):
            player = self.loadPlayer(os.path.join(
                players_path, file, "ncaaf.csv"))
            for pos in player.keys():
                if pos not in by_position.keys():
                    by_position[pos] = []
                by_position[pos].append(player[pos])
        self.by_position = by_position

    def from_file(self):
        pass

    def read_applicables(self, applicable_path):
        applicables = {}
        for filename in os.listdir(applicable_path):
            with open(os.path.join(applicable_path, filename)) as applicable:
                applicable_stats = list(
                    map(lambda x: x.strip(), applicable.read().split(",")))
                applicables[filename.split('.')[0]] = applicable_stats
        return applicables

    def dump_datasets(self, out_path):
        os.makedirs(out_path, exist_ok=True)
        print("TEST")
        for position in self.by_position.keys():
            print(position)
            self.load_dataset(position).to_csv(
                os.path.join(out_path, position + '.csv'))

    def __init__(self, method='gathered', dump=False, applicable_path=os.path.join('applicable'), players_path=os.path.join('pairedPlayers'), dataset_path=os.path.join('datasets'), out_path=os.path.join('out', 'datasets', datetime.datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S"))):
        self.method = method
        if self.method == 'gathered':
            self.applicables = self.read_applicables(applicable_path)
            self.from_gathered(players_path)
            if dump:
                self.dump_datasets(out_path)
        elif self.method == 'file':
            self.dataset_path = dataset_path
            self.from_file()


if __name__ == "__main__":
    loader = Dataset_Loader(dump=True)
    # print(loader.loadPlayer("pairedPlayers/AbduAm00/ncaaf.csv"))
    print(loader.load_dataset("QB"))
