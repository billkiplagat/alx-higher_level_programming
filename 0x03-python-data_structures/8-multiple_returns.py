#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        # Meaning we have a sentence
        first_chr = sentence[0]
    else:
        first_chr = None
    return length, first_chr
