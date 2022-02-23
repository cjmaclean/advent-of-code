import sys

file_name = sys.argv[1]
print("accessing file: ", file_name)

file = open(file_name, 'r')
lines = file.readlines();

first_line = True
counted_increases = 0

for line in lines:
    depth = int(line)
    if not first_line:
        if depth > previous_depth:
            counted_increases += 1  
  
    # get ready for next iteration:
    first_line = False
    previous_depth = depth
    
print(counted_increases)