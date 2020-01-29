import csv
from sportsreference.nfl.teams import Teams as nflTeams
from sportsreference.ncaaf.teams import Teams as ncaafTeams
from sportsreference.nfl.roster import Player as nflPlayer
from sportsreference.ncaaf.roster import Player as ncaafPlayer
from bs4 import BeautifulSoup
from urllib.request import urlopen as req
import re
import requests
import pandas as pd
import numpy as np
import os

for nflTeam in nflTeams():
    roster = nflTeam.roster
    for player in roster.players:
        nfl_id = player.player_id
        print(player.name)
        # get college ID from NFL ID
        url = "https://www.pro-football-reference.com/players/" + nfl_id[0] + "/" + nfl_id + ".htm"

        uClient = req(url)
        page_html = uClient.read()
        uClient.close()

        soup = BeautifulSoup(page_html, "html.parser")

        try:
            linkText = soup.find("a", text=re.compile(r'College Stats'))["href"]
            print(linkText)
        except:
            continue

        if linkText:
            college_id_html = linkText.split('/players/')[1]
            college_id = college_id_html.split('.')[0]

            player_got = ncaafPlayer(college_id)
        else:
            break
        try:
            print("NFL id " + player.player_id + " NCAAF id: " + college_id)
            ## NEED TO HAVE THIS PORTION NOT BE PRINT OUT ONLY, HERE WE CAN USE THE ID TO GET THE INFO FROM THE NCAAF DATABASE ##
            # try:
            print("NFL Player: " + player.name + ", NCAAF Player: " + player_got.name)

            os.mkdir('/Users/brandonschein/PycharmProjects/SeniorCapstone/pairedPlayers/' + player.player_id)

            #college#
            path = '/Users/brandonschein/PycharmProjects/SeniorCapstone/pairedPlayers/' + player.player_id + '/nfl.csv'
            player.dataframe.to_csv(path)

            #NFL#
            path = '/Users/brandonschein/PycharmProjects/SeniorCapstone/pairedPlayers/' + player.player_id + '/ncaaf.csv'
            player_got.dataframe.to_csv(path)

        except:
            print("Error on player " + player.player_id)
