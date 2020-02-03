#!/usr/bin/env python3
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
import logging
import datetime
import os


def getNcaafPlayer(nflId):
    url = "https://www.pro-football-reference.com/players/" + \
        nflId[0] + "/" + nflId + ".htm"

    uClient = req(url)
    page_html = uClient.read()
    uClient.close()

    soup = BeautifulSoup(page_html, "html.parser")

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


def writePlayer(playerNfl, playerNcaaf, outputDir):
    try:
        if playerNfl.dataframe is None or playerNcaaf.dataframe is None:
            raise Exception("No dataframe")
        playerOut = os.path.join(outputDir, playerNfl.player_id)

        os.makedirs(playerOut)

        path = os.path.join(playerOut, "nfl.pkl")
        playerNfl.dataframe.to_pickle(path)

        path = os.path.join(playerOut, "ncaaf.pkl")
        playerNcaaf.dataframe.to_pickle(path)

    except:
        logging.warning("No dataframe for player %s. Skipping..." %
                        playerNfl.name)


def processTeam(nflTeam, outputDir):
    roster = nflTeam.roster
    logging.info("Processing roster for team %s" % nflTeam.name)
    for playerNfl in roster.players:
        nflId = playerNfl.player_id
        logging.info("Processing player %s" % playerNfl.name)
        playerNcaaf = getNcaafPlayer(nflId)
        if playerNcaaf is not None:
            writePlayer(playerNfl, playerNcaaf, outputDir)


def main():
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S")
    if not os.path.exists("logs"):
        os.makedirs("logs")
    logging.basicConfig(filename="logs/%s.log" %
                        timestamp, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
    logging.info("Began running data gatherer at %s" % timestamp)
    outputDir = os.path.join("out", timestamp)
    os.makedirs(outputDir)
    nflTeamList = nflTeams()
    logging.info("Successfully fetched NFL Team list from API")

    for nflTeam in nflTeamList:
        processTeam(nflTeam, outputDir)


if __name__ == "__main__":
    main()
