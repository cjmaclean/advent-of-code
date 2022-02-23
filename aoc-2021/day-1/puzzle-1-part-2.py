import sys

file_name = sys.argv[1]
print("accessing file: ", file_name)

file = open(file_name, 'r')
lines = file.readlines();

first_sum = True
counted_increases = 0

depth_list = []
i = 0 #index into list

for line in lines:
    if i >= 3:
        first_sum = False
        previous_depth_sum = depth_sum

    depth = int(line)
    depth_list.append(depth)
    if i >= 2: # 3rd or later item, with zero-indexing
        depth_sum = depth_list[i] + depth_list[i-1] + depth_list[i-2]

    if not first_sum:
        if depth_sum > previous_depth_sum:
            counted_increases += 1  
  
    # get ready for next iteration:
    i += 1
    
print(counted_increases)