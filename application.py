import constants
from copy import deepcopy

PLAYERS = deepcopy(constants.PLAYERS)

TEAMS = deepcopy(constants.TEAMS)

allocated_teams = []
allocated_players = []

def clean_data(collection):
    '''This is function that will take a collection and
    it will clean up the heights key with a value containing number and
     store them as integer
    And if the experience value is Yes/NO it will save the value as true/false
    '''

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

    num_players_team = len(players) / len(teams)

    for team in teams:
        count = 0
        # create a dictionary with team name and append 6 players data into a team
        allocated_teams.append({'team name': '{}'.format(team)})
        list = []
        copy_of_players = players[::]

        while count < num_players_team:
            list.append(copy_of_players.pop())
            count += 1
        allocated_players.append(list)

def display_team_print(option, teams, players):
    option_index = option - 1
    team_name = str(teams[option_index].values()).strip('[]')
    players_string = []
    print(
        '''
        Team: {} Stats
        --------------------
        Total players: {}

        Players on Team:
        '''.format(team_name, len(players[option_index]) )
        )
    for player in players[option_index]:
        players_string.append((player['name']))

    print(', '.join(players_string))


if __name__ == "__main__":
    clean_data(PLAYERS)
    balance_teams(TEAMS, PLAYERS)

    print('BASKETBALL TEAM STATS TOOL')
    print('\n---- MENU----')
    print("""
    Here are your choices:
    1) Display Team Stats
    2) Quit
    """)
    display_stats = input("Enter an option > ")
    if display_stats == 1:
        list_number = 1
        for team in allocated_teams:
            print('{}) {}'.format(list_number, str(team.values()).strip('[]')))
            list_number += 1
        display_team = input("Enter an option > ")
        display_team_print(display_team, allocated_teams, allocated_players)
        print('Press ENTER to continue...')
