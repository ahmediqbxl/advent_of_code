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
            data_list.append(line.strip())

    data_list = [item for item in data_list if item != 'Game']

    return data_list

# Step 2: Structure the data into a dictionary
def structure_games(data):
    # Initialize variables
    game_dict = {}
    current_game = None
    current_set = None
    current_color = None

    for item in data:
        if item.isdigit():
            if current_game is None:
                current_game = int(item)
                game_dict[current_game] = {}
            elif current_set is None:
                current_set = f'set {item}'
                game_dict[current_game][current_set] = {}
        elif item.endswith(';'):
            current_color = item.rstrip(';')
        elif item.isalpha():
            game_dict[current_game][current_set][current_color] = item

    return game_dict

data = read_text_file('sample_input.txt')
data_dict = structure_games(data)

print(data)