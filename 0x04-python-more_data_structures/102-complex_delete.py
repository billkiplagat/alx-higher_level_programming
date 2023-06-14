#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = []
    for key in a_dictionary.keys():
        if value in a_dictionary[key]:
            # to prevent dictionary from changing size during iteration
            keys_to_delete.append(key)

    for k in keys_to_delete:
        del a_dictionary[k]
    return a_dictionary
