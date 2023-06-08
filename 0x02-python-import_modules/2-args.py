#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argument = sys.argv[1:]
    args_num = len(argument)
    index = 1
    if args_num == 1:
        print("{} argument:".format(args_num))
    else:
        print("{} arguments:".format(args_num))
    for i in argument:
        print("{}: {}".format(index, i))
        index = index + 1
