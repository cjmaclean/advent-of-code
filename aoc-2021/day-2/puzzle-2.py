import sys

file_name = sys.argv[1]
print("accessing file: ", file_name)

file = open(file_name, 'r')
lines = file.readlines()

horizontal_position = 0
depth = 0

for line in lines:
    # read command and adjust position
    print(line)

print("Result:")
print(horizontal_position * depth)