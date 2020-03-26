#!/usr/bin/env python3
import os
import csv
import logging
import datetime

PLAYER_DIR = os.path.join(os.curdir, "pairedPlayers")


def extractPos(file, globalStats):
    with open(file, mode='r') as infile:
        reader = csv.DictReader(infile)
        # print(reader.fieldnames)
        positions = {}
        for row in reader:
            positions[row["position"]] = set(filter(
                lambda x: row[x] != "", reader.fieldnames)).difference(globalStats)
        return positions


def readGlobals(globalStatPath):
    with open(globalStatPath) as f:
        return set(list(csv.reader(f))[0])


def writePos(pos, playerPos, outputDir):
    outPath = os.path.join(outputDir, pos + ".csv")
    with open(outPath, 'w', newline='') as outFile:
        wr = csv.writer(outFile)
        wr.writerow(playerPos)


def main():
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S")
    os.makedirs(os.path.join(os.curdir, "logs", "positions"), exist_ok=True)
    logging.basicConfig(filename=os.path.join("logs", "positions", timestamp + ".log"),
                        format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
    logging.info("Began running position extractor at %s" % timestamp)
    outputDir = os.path.join(os.curdir, "out", "positions", timestamp)
    os.makedirs(outputDir, exist_ok=True)
    parsedPos = dict()
    indirectory = os.fsencode(PLAYER_DIR)
    globalStats = readGlobals(os.path.join(os.curdir, "global_stat_ncaaf.csv"))
    logging.info("Read global stats")
    for file in os.listdir(indirectory):
        filename = os.fsdecode(file)
        playerPath = os.path.join(
            PLAYER_DIR, filename, "ncaaf.csv")
        playerPositions = extractPos(playerPath, globalStats)
        logging.info("Reading player info from %s" % playerPath)
        for pos in playerPositions.keys():
            logging.info("Checking position %s " % pos)
            print(pos, parsedPos, playerPositions[pos])
            input()
            if pos in parsedPos.keys():
                parsedPos[pos].intersection_update(playerPositions[pos])
            else:
                parsedPos[pos] = playerPositions[pos]
        logging.info("Finished checking all players. Dumping...")
        for pos in parsedPos.keys():
            writePos(pos, parsedPos[pos], outputDir)
            logging.info("Wrote out file for %s" % pos)


if __name__ == "__main__":
    main()
