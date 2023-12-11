'''Solution to Advent of Code day 2'''
'''Determine which games would have been possible if the bag had been loaded with only 
12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?'''

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
def structure_data(data):
    split_data = split_on_colons(data)
    split_data_new = split_on_semicolons(split_data)

    data_dict = dict(split_data_new)

    result = {key: [dict(entry.strip().split(' ', 1) 
                        for entry in value.split(',')) for value in data_dict[key]] for key in data_dict}
    
    return result

# Step 3: Figure out which games are possible
def analyze_games(data_dict):
    count = 0 
    loaded_cubes = {
        'red':'12',
        'green':'13',
        'blue':'14'
    }

    for key, value in data_dict.items():
        impossible = False
        for set in value: # value is a list that contains the set as a dictionary
            for number, color in set.items(): # 7, red
                constraint_value = loaded_cubes[color]
                if int(constraint_value) < int(number):
                    impossible = True # we can't add this into the count
        if impossible:
            print(f"Game {key} is not possible")
        else:
            print(f"Game {key} is possible")
            count = count + int(key)
    return count


data = read_text_file('input.txt')

result = structure_data(data)

count = analyze_games(result)

print("Sum of ID's that are possible is", count) # 2447