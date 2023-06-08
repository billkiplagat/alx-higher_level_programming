#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = sys.argv[1:]
    total = 0
    for i in argument:
        i = int(i)
        total += i

    print(total)
