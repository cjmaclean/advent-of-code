import sys

file_name = sys.argv[1]
print("accessing file: ", file_name)

file = open(file_name, 'r')
lines = file.readlines()

first_line = True

# Counters will be a list of dictionaries.
# First item in list, counters[0] has the counters for
# the first bit position.
# counters[0]["1"] is the counter for how many "1"
# characters are in the first bit position

counters = [] # empty until first line is read

for line in lines:
    line = line.rstrip("\n") # remove newline character
    # print(line)
    if first_line:
        # initialise counters to all zeros
        for bit in line:
            counters.append({"0": 0, "1": 0})
            # print("bit:"+bit+"."+"code:",ord(bit))
            # print(int(bit))

    for index,bit in enumerate(line):
        counters[index][bit] += 1
        # print("index:",index,"bit:"+bit+"."+"code:",ord(bit))
        # print(int(bit))
        
    first_line = False

print("Result:")
print("...")
for index,counters_here in enumerate(counters):
    counter_0 = counters_here["0"]
    counter_1 = counters_here["1"]
    print("index:",index)
    print("0's:",counter_0)
    print("1's:",counter_1)
