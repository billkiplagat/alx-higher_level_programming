#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    modules = sorted(dir(hidden_4))
    for i in modules:
        if i[:2] != '__':
            print("{}".format(i))
