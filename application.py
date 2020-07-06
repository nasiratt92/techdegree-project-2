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
        allocated_teams.append('{}'.format(team))
        list = []
        copy_of_players = players[::]

        while count < num_players_team:
            list.append(copy_of_players.pop())
            count += 1
        allocated_players.append(list)

def display_team_print(option, teams, players):
    option_index = option - 1
    team_name = str(teams[option_index])
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
    #while True:
    valid_input = False
    while not valid_input:
        display_stats = input("Enter an option > ")
        try:
            display_stats = int(display_stats)
        except ValueError:
            print("ValueError: please enter 1 or 2 ")
        else:
            if display_stats != 1 and display_stats != 2:
                raise Exception("Sorry, numbers 1 or 2 are the only availible options")
                continue
            else:
                valid_input = True

    if display_stats == 1:
        list_number = 1
        for team in allocated_teams:
            print('{}) {}'.format(list_number, team))
            list_number += 1
        #display_team = int(input("Enter an option > "))

        valid_input = False
        number_of_teams = len(allocated_teams)
        while not valid_input:
            display_team = int(input("Enter an option > "))
            try:
                display_stats = int(display_stats)
            except ValueError:
                print("ValueError: please enter a number between 1 to {}".format( number_of_teams))
            else:
                if display_stats <= 0 or display_stats > number_of_teams:
                    raise Exception("Sorry, only numbers between 1 to {} are the availible options".format(number_of_teams))
                    continue
                else:
                    valid_input = True



        display_team_print(display_team, allocated_teams, allocated_players)
        print('Press ENTER to continue...')
    elif display_stats == 2:
        exit()
