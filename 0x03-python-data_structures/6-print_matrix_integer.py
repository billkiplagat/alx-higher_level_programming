#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        # enumerate function to iterate over the elements in each row
        for row_index, value in enumerate(row):
            if row_index != len(row) - 1:
                print("{} ".format(value), end="")
            else:
                print("{}".format(value), end="")
        print()
