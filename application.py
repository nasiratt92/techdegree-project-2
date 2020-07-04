import constants
import pdb

# dunder_main at the end

# write collection cleaning function
PLAYERS = constants.PLAYERS
TEAMS = constants.TEAMS


def clean_data(collection):
    '''This is function that will take a collection and return a new collection
    it will clean up all the strings containing number and store them as integers
    in the new collection.
    And if the value is Yes/NO it will save the value as true/false in the return
    collection'''
    for dictionary in collection:

        for key, value in dictionary.items():
            if key == 'height':
            #    pdb.set_trace()
                dictionary[key] = int(value[0:2])
            elif key == 'experience':
                if value == 'YES':
                    dictionary[key] = True
                else:
                    dictionary[key] = False

def balance_teams(teams, players):

    allocated_teams = []
    allocated_players = []

    num_players_team = len(players) / len(teams)

    for team in teams:
        count = 0
        # create a dictionary with team name and append 6 players data into a team
        allocated_teams.append({'team name': '{}'.format(team)})
        list = []
        while count < num_players_team:
            list.append(players.pop())
            count += 1
        allocated_players.append(list)

    return allocated_players    


clean_data(PLAYERS)
balance_teams(TEAMS, PLAYERS)
print(allocated_teams)
print(len(allocated_players[0]))
