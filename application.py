import constants
from copy import deepcopy

PLAYERS = deepcopy(constants.PLAYERS)

TEAMS = deepcopy(constants.TEAMS)

allocated_teams = []
allocated_players = []
players_string = []
user_input = 0

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
    print('i am here')
    print(num_players_team)

    copy_of_players = deepcopy(players)
    for team in teams:
        count = 0
        # create a dictionary with team name and append 6 players data into a team
        allocated_teams.append('{}'.format(team))
        list = []
        while count < num_players_team:
            list.append(copy_of_players.pop())
            count += 1
        allocated_players.append(list)

def display_team_print(option, teams, players):
    option_index = option - 1
    team_name = str(teams[option_index])

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

def get_int_from_user(max_int):
    #I am adding 1 to the max_int so I can get the end index for the the range() function
    max_int += 1
    # I am using list comprehensions here to generate the string ! Yes!

    strings_list = [str(integer) for integer in range(1, max_int)]

    options_string = ", ".join(strings_list)

    valid_input = False
    while not valid_input:
        user_input = input("Enter an option > ")
        try:
            user_input = int(user_input)
        except ValueError:
            print("ValueError: please enter one of the following: {}".format(options_string))

        else:
            if user_input > 0 and user_input <= max_int:
                # use range function to list options

                valid_input = True

            else:
                print("Sorry, only numbers {} are the availible options".format(options_string))
    return user_input
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

    user_input = get_int_from_user(2)

    if user_input == 1:
        list_number = 1
        for team in allocated_teams:
            print('{}) {}'.format(list_number, team))
            list_number += 1
        display_team = get_int_from_user(len(allocated_teams))

        display_team_print(display_team, allocated_teams, allocated_players)

        print('Press ENTER to continue...')

    elif user_input == 2:
        exit()
