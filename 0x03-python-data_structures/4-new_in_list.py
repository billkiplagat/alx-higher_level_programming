#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    modified_list = []
    for i in my_list:
        if i == my_list[idx]:
            modified_list.append(element)
        else:
            modified_list.append(i)
    return modified_list
