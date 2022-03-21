import sys

file_name = sys.argv[1]
print("accessing file: ", file_name)

file = open(file_name, 'r')
lines = file.readlines()


for line in lines:
    print(line)

print("Result:")
print("...")