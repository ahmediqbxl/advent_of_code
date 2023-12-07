'''Solution to Advent of Code day 1'''

# Step 1: Read in the input file as a list
def read_text_file(file):
    data_list = []

    with open(file, "r") as f:
        for line in f:
            data_list.extend(line.split())

    return data_list

def calculate_calibration_value_first_digit(word):
    calibration_value = 0
    for w in word: # go from right to left to find first numeric value using isnumeric(). 
                   # this needs to be multiplied by 10 since its the first figit
        if w.isnumeric():
            calibration_value += (int(w)*10)
            break

    return calibration_value

def calculate_calibration_value_second_digit(word):
    calibration_value = 0
    reversed_word = reversed(word)

    for w in reversed_word:
        if w.isnumeric():
            calibration_value += int(w)
            break

    return calibration_value

# Step 2: Define logic to calculate calibration value for each word
def calculate_calibration_value(word):
    first_digit = calculate_calibration_value_first_digit(word)
    second_digit = calculate_calibration_value_second_digit(word)

    return first_digit+second_digit

# Step 3: Iterate over list of input words and calculate calibration values
def summarize_calibration_values(file):
    inputs = read_text_file(file) # list of inputs
    total = 0 
    for word in inputs:
        calibration_value = calculate_calibration_value(word)
        total += calibration_value

    return total

if __name__ == "__main__":
    text_file = 'input.txt'
    total = summarize_calibration_values(text_file)
    print("The total is: ", total) # answer is 53651
