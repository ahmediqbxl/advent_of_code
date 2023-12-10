'''Solution to Advent of Code day 1 Part 2'''

import re

word_to_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

# Step 1: Read in the input file as a list
def read_text_file(file):
    data_list = []

    with open(file, "r") as f:
        for line in f:
            data_list.extend(line.split())
    return data_list

def is_key_in_string(dictionary, input_string):
    for key in dictionary.keys():
        if input_string.startswith(key):
            return True
    return False

def replace_keys_with_values(dictionary, input_string):
    for key, value in dictionary.items():
        if key in input_string:
            input_string = input_string.replace(key, str(value))
    return input_string

# Step 2: Replace "numeric words" with actual digits
def standarize_word(text):
    if is_key_in_string(word_to_digit, text):
        text = replace_keys_with_values(word_to_digit, text)
    return text
    
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

# Step 3: Define logic to calculate calibration value for each word
def calculate_calibration_value(word):
    first_digit = calculate_calibration_value_first_digit(word)
    second_digit = calculate_calibration_value_second_digit(word)
    print(first_digit, " | ", second_digit)

    return first_digit+second_digit

# Step 3: Iterate over list of input words and calculate calibration values
def summarize_calibration_values(file):
    inputs = read_text_file(file) # list of inputs
    total = 0 
    for word in inputs:
        standarized_word = standarize_word(word)
        print(standarized_word)
        calibration_value = calculate_calibration_value(standarized_word)
        total += calibration_value

    return total

if __name__ == "__main__":
    text_file = 'sample_input.txt'
    total = summarize_calibration_values(text_file)
    print("The total is: ", total) # answer is 281
