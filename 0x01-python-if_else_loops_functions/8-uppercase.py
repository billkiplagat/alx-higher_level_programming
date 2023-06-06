#!/usr/bin/python3
def uppercase(str):
    converted_text = ""
    for char in str:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:
            # chr() returns a string representing a character whose
            # Unicode code point is the specified integer
            converted_char = chr(ascii_val - 32)
        else:
            converted_char = char
        converted_text += converted_char
    print("{}".format(converted_text))
