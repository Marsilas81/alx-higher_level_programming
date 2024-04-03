#!/usr/bin/python3

# Define a function named safe_print_list
# Parameters:
#   - my_list: The list to print elements from (default value is an empty list)
#   - x: The number of elements to print (default value is 0)
# Returns: The real number of elements printed

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end=" ")
            count += 1
    except:
        continue
    print()
    return count
