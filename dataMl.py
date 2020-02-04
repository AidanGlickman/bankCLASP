#!/usr/bin/env python3
import sklearn
import os
import logging
import pandas as pd
import numpy as np


# scaler = sklearn.preprocessing.StandardScaler()
# scaler.fit(data_train)
# data_train = scaler.transform(data_train)
# data_test = scaler.transform(data_test)
# data_val = scaler.transform(data_val)

PLAYER_DIR = "./pairedPlayers"

if not os.path.exists(PLAYER_DIR):
    logging.critical("Player Directory doesn't exist. Please reconfigure it.")


def playerToDataPoint(playerPath):
    data = pd.read_csv(playerPath)
    print(data)


def findNearestPlayers(player, dataset, numPlayers=5):
    """Return numPlayers players from dataset with highest cosine similarity to player"""
    pass


def main():
    playerToDataPoint("out/2020-02-03-17:18:44/AndrMa00/ncaaf.pkl")


if __name__ == "__main__":
    main()
