#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0]
    if sentence is None:
        first_char = None
    new_tuple = (length, first_char)
    return new_tuple
