#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    index = 0
    for j in str:
        if index != n:
            new_str = new_str + j
        index += 1
    return new_str
