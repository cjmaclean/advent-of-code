import sys

file_name = sys.argv[1]
print("accessing file: ", file_name)

file = open(file_name, 'r')
all_lines = file.readlines()
line_length = len(all_lines[0].rstrip("\n"))


def most_common_bit(lines, position):

    # Counter will be a dictionary.
    # counter["0"] is the counter for how many "0"
    # characters are in the selected bit position
    # counter["1"] is the counter for how many "1"
    # characters are in the selected bit position

    counter = {"0": 0, "1": 0}

    for line in lines:
        line = line.rstrip("\n") # remove newline character
        # print(line)

        bit = line[position]
        counter[bit] += 1
        # print(int(bit))

    counter_0 = counter["0"]
    counter_1 = counter["1"]

    if counter_0 > counter_1:
        return "0"
    elif counter_1 > counter_0:
        return "1"
    else:
        print("neither is greater, defaulting to 1")
        return "1"

def least_common_bit(lines, position):
    most_common = most_common_bit(lines, position)
    if most_common == "0":
        return "1"
    elif most_common == "1":
        return "0"
    else:
        print("error converting most common to least common")

def filter_keep(lines, position, bit):
    kept_lines=[]
    for line in lines:
        if line[position] == bit:
            kept_lines.append(line)
    return kept_lines

# first keep the lines with the most common bit
lines_remaining = all_lines
for bit_position in range(0,line_length):
    if len(lines_remaining) > 1:
        keep_bit = most_common_bit(lines_remaining, bit_position)
        lines_remaining = filter_keep(lines_remaining, bit_position, keep_bit)

oxygen_line = lines_remaining[0]

# next keep the lines with the least common bit
lines_remaining = all_lines
for bit_position in range(0,line_length):
    if len(lines_remaining) > 1:
        keep_bit = least_common_bit(lines_remaining, bit_position)
        lines_remaining = filter_keep(lines_remaining, bit_position, keep_bit)

co2_line = lines_remaining[0]

oxygen_rating = 0
co2_rating = 0

for index in range(line_length):
    o_bit = oxygen_line[index]
    co2_bit = co2_line[index]
    # last digit is digit 0, calculate digit number
    digit_number = line_length - 1 - index
    digit_multiplier = 2 ** digit_number

    if o_bit == "1":
        oxygen_rating += digit_multiplier
    if co2_bit == "1":
        co2_rating += digit_multiplier

print("Result:", oxygen_rating, "*", co2_rating, "=", co2_rating * oxygen_rating)


