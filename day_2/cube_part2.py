'''Solution to Advent of Code day 2 part 2
For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?'''

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

    result = {key: [dict(entry.strip().split(' ', 1) for entry in pair.split(',')) for section in data_dict[key] for pair in section.split(';')] for key in data_dict}

    return result

# Step 3: Figure out which games are possible
def analyze_games(data_dict):
    count = 0 

    for key, value in data_dict.items():
        loaded_cubes = {
            'red':0,
            'green':0,
            'blue':0
        }
        for set in value: # value is a list that contains the set as a dictionary
            for number, color in set.items(): # 7, red
                loaded_value = loaded_cubes[color] # starts at 0
                if loaded_value < int(number): # finding minimum value and assign it to color
                    loaded_cubes[color] = int(number)

        # at this point, the set has the minimum values of colors
        power = loaded_cubes['blue']*loaded_cubes['green']*loaded_cubes['red']
        print("power is ", loaded_cubes)
        count = count + power

    return count

data = read_text_file('sample_input.txt')

result = structure_data(data)

count = analyze_games(result)

print(count)


# there's a bug that isn't reading in one color from the last set. Need to 
# review the structure_data function. 