import constants

# dunder_main at the end

# write collection cleaning function

def value_pair_cleaner(collection):
    '''This is function that will take a collection and return a new collection
    it will clean up all the strings containing number and store them as integers
    in the new collection.
    And if the value is Yes/NO it will save the value as true/false in the return
    collection'''
    for dictionary in collection:
        for key, value in dictionary.items():
            print(dictionary[key])

value_pair_cleaner(constants.PLAYERS)
