'''Solution to Advent of Code day 1'''


# Step 1: Read in the input file as a list
def read_text_file(file):
    input_file = open(file, "r")
    data = input_file.read()

    return data

# reverse the word
def reverse_slicing(s):
    return s[::-1]

# Step 2: Define logic to calculate calibration value for each word
def calculate_calibration_value(word):
    # go from left to right to find first numeric value using isnumeric()
    calibration_value = 0
    for w in word: # go from right to left to find first numeric value using isnumeric()
        if w.isnumeric():
            calibration_value += int(w)
            break

    for w in reverse_slicing(word):
        if w.isnumeric():
            calibration_value += int(w)
            break

    return calibration_value

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
    print("The total is: ", total) # total is 21560 based on this program