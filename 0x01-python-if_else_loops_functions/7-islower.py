#!/usr/bin/python3
def islower(c):
    # To obtain the ASCII value of the letter
    asi = ord(c)
    if 97 <= asi <= 122:
        return True
    else:
        return False
