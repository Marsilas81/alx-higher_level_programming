#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safely prints the first x elements of a list.

    Args:
        my_list (list): The list to print elements from. Defaults to an empty list.
        x (int): The number of elements to print. Defaults to 0.

    Returns:
        int: The real number of elements printed.
    """
    count = 0  # Initialize a counter to track the number of elements printed
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end=" ")  # Print the current element
            count += 1  # Increment the counter
    except IndexError:
        pass  # If an IndexError occurs (e.g., x is greater than the length of my_list), do nothing
    finally:
        print()  # Print a newline after printing all elements (even if an exception occurs)
    return count  # Return the total number of elements printed

