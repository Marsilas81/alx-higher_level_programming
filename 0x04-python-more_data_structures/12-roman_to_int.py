#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = prev_value = 0

    for symbol in reversed(roman_string):
        value = roman_dict[symbol]
        result += value if value >= prev_value else -value
        prev_value = value

    return result

# Test cases
if __name__ == "__main__":
    test_cases = ["X", "VII", "IX", "LXXXVII", "DCCVII"]
    for roman_number in test_cases:
        print("{} = {}".format(roman_number, roman_to_int(roman_number)))
