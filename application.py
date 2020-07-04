import constants
import pdb

# dunder_main at the end

# write collection cleaning function
PLAYERS = constants.PLAYERS

def value_pair_cleaner(collection):
    '''This is function that will take a collection and return a new collection
    it will clean up all the strings containing number and store them as integers
    in the new collection.
    And if the value is Yes/NO it will save the value as true/false in the return
    collection'''
    for dictionary in collection:

        for key, value in dictionary.items():
            if key == 'height':
            #    pdb.set_trace()
                dictionary[key] = value[1:3]
            elif key == 'experience':
                if value == 'YES':
                    dictionary[key] = True
                else:
                    dictionary[key] = False

            print('{}: {}'.format(key, value))

value_pair_cleaner(PLAYERS)
