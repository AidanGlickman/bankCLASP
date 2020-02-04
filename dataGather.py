#!/usr/bin/env python3
import csv
from sportsreference.nfl.teams import Teams as nflTeams
from sportsreference.ncaaf.teams import Teams as ncaafTeams
from sportsreference.nfl.roster import Player as nflPlayer
from sportsreference.ncaaf.roster import Player as ncaafPlayer
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
import numpy as np
import logging
import datetime
import os


def getNcaafPlayer(nflId):
    """Returns an ncaafPlayer object by scraping an nflPlayer's PFR page"""
    url = "https://www.pro-football-reference.com/players/" + \
        nflId[0] + "/" + nflId + ".htm"

    page = requests.get(url).text

    soup = BeautifulSoup(page, "html.parser")

    try:
        linkText = soup.find(
            "a", text=re.compile(r'College Stats'))["href"]
        collegeIdHtml = linkText.split('/players/')[1]
        collegeId = collegeIdHtml.split('.')[0]

        return ncaafPlayer(collegeId)
    except:
        logging.warning(
            "Failed to get college link for player %s. Skipping..." % nflId)
        return None


def writePlayer(player, outputDir):
    """Writes out the data for a given player to outputDir"""
    try:
        if player["nfl"].dataframe is None or player["ncaaf"].dataframe is None:
            raise Exception("No dataframe")
        playerOut = os.path.join(outputDir, player["nfl"].player_id)

        os.makedirs(playerOut)

        path = os.path.join(playerOut, "nfl.csv")
        player["nfl"].dataframe.to_csv(path)

        path = os.path.join(playerOut, "ncaaf.csv")
        player["ncaaf"].dataframe.to_csv(path)

    except:
        logging.warning("No dataframe for player %s. Skipping..." %
                        player["nfl"].name)


def processTeam(nflTeam, outputDir):
    """Processes each player on a given nflTeam, outputs to outputDir"""
    roster = nflTeam.roster
    logging.info("Processing roster for team %s" % nflTeam.name)
    player = {}
    for playerNfl in roster.players:
        player["nfl"] = playerNfl
        nflId = player["nfl"].player_id
        logging.info("Processing player %s" % player["nfl"].name)
        player["ncaaf"] = getNcaafPlayer(nflId)
        if player["ncaaf"] is not None:
            writePlayer(player, outputDir)


def main():
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S")
    if not os.path.exists("logs"):
        os.makedirs("logs")
    logging.basicConfig(filename="logs/%s.log" %
                        timestamp, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
    logging.info("Began running data gatherer at %s" % timestamp)
    outputDir = os.path.join("out", timestamp)
    os.makedirs(outputDir)
    nflTeamList = nflTeams()
    logging.info("Successfully fetched NFL Team list from API")

    for nflTeam in nflTeamList:
        processTeam(nflTeam, outputDir)


if __name__ == "__main__":
    main()
