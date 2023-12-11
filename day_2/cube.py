'''Solution to Advent of Code day 2'''
'''Determine which games would have been possible if the bag had been loaded with only 
12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?'''

loaded_cubes = {
    'red':'12',
    'green':'13',
    'blue':'14'
}


# Step 1: Read in the input file as a list
def read_text_file(file):
    data_list = []

    with open(file, "r") as f:
        for line in f:
            line = line.replace('Game', '')
            data_list.append(line.strip())

    return data_list

def split_on_colons(data):
    split_data = []
    for line in data:
        new_line = line.split(":")
        split_data.append(new_line)

    return split_data

def split_on_semicolons(data):
    for line in data: # data is now a list of lists with the first item being the game value
        values = line[1]
        split_set = values.split(";")
        line[1] = split_set
    
    return data

# Step 2: Structure the data into a dictionary
def structure_games(data):
    # Initialize variables
    game_dict = {}
    current_game = None
    current_set = None
    current_color = None

    for line in data: 
        # Split the string into tokens
        tokens = line.split()

        for token in tokens:
            if token.isdigit():
                if current_game is None:
                    current_game = int(token)
                    game_dict[current_game] = {}
                elif current_set is None:
                    current_set = f'set {token}'
                    game_dict[current_game][current_set] = {}
            elif token.endswith(';'):
                current_color = token.rstrip(';')
            elif token.isalpha():
                if current_color is not None:
                    game_dict[current_game][current_set][current_color] = int(token)
        
    return game_dict

data = read_text_file('sample_input.txt')
# data_dict = structure_games(data)

split_data = split_on_colons(data)
split_data_new = split_on_semicolons(split_data)

print(dict(split_data_new))
