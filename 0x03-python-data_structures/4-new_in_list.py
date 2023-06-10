#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    if idx < 0:
        return my_list
    if idx < len(my_list):
        modified_list = []
        for i in my_list:
            if i == my_list[idx]:
                modified_list.append(element)
            else:
                modified_list.append(i)
        return modified_list
    return my_list
