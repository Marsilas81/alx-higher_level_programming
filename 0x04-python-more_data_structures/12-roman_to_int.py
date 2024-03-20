#!/usr/bin/python3

# Converts a Roman numeral to an integer.
def roman_to_int(roman_string):
    roman_values = [1, 5, 10, 50, 100, 500, 1000]
    roman_symbols = 'IVXLCDM'

    num = 0
    prev_value = 0

    for symbol in reversed(roman_string):
        value = roman_values[roman_symbols.index(symbol)]
        if value < prev_value:
            num -= value
        else:
            num += value
        prev_value = value

    return num


if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
