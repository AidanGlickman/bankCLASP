import csv
from sportsreference.nfl.teams import Teams as nflTeams
from sportsreference.ncaaf.teams import Teams as ncaafTeams
from sportsreference.nfl.roster import Player as nflPlayer
from sportsreference.nfl.roster import Player as ncaafPlayer
import os


for nflTeam in nflTeams():
    roster = nflTeam.roster
    for player in roster.players:
        id_to_get = player.player_id
        player_got = ncaafPlayer(id_to_get)
        print("NFL id " + player.player_id + " NCAAF id: " + id_to_get)
        ## NEED TO HAVE THIS PORTION NOT BE PRINT OUT ONLY, HERE WE CAN USE THE ID TO GET THE INFO FROM THE NCAAF DATABASE ##
        try:
            print("NFL Player: " + player.name + ", NCAAF Player: " + player_got.name)

            os.mkdir('/Users/brandonschein/PycharmProjects/SeniorCapstone/pairedPlayers/' + player.player_id)

            #college#
            path = '/Users/brandonschein/PycharmProjects/SeniorCapstone/pairedPlayers/' + player.player_id + '/ncaaf.csv'
            player.dataframe.to_csv(path)

            #NFL#
            path = '/Users/brandonschein/PycharmProjects/SeniorCapstone/pairedPlayers/' + player.player_id + '/nfl.csv'
            player_got.dataframe.to_csv(path)
            
        except:
            print("Error on player " + player.player_id)
