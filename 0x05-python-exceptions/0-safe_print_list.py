#!/usr/bin/python3

# Define a function named safe_print_list
# Parameters:
#   - my_list: The list to print elements from (default value is an empty list)
#   - x: The number of elements to print (default value is 0)
# Returns: The real number of elements printed
def safe_print_list(my_list=[], x=0):
    count = 0  # Initialize a counter to track the number of elements printed
    try:
        for i in range(x):  # Iterate through the first x elements of my_list
            print("{}".format(my_list[i]), end=" ")  # Print the current element
            count += 1  # Increment the counter
    except IndexError:
        pass  # If an IndexError occurs (e.g., x is greater than the length of my_list), do nothing
    finally:
        print()  # Print a newline after printing all elements (even if an exception occurs)
    return count  # Return the total number of elements printed

