import sys

file_name = sys.argv[1]
print("accessing file: ", file_name)

file = open(file_name, 'r')
lines = file.readlines()

horizontal_position = 0
depth = 0

for line in lines:
    # read command and adjust position
    # print(line)
    words = line.split()
    # print(words)
    command_name = words[0]
    command_amount = int(words[1])
    print(command_name, command_amount)
    if command_name == "forward":
        horizontal_position += command_amount
    elif command_name == "down":
        depth += command_amount
    elif command_name == "up":
        depth -= command_amount
    else:
        print("unknown command ", command_name)
    print(horizontal_position, depth)


print("Result:")
print(horizontal_position * depth)