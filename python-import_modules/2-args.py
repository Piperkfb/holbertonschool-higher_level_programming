#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    cnt = len(argv) - 1
    if cnt == 0:
        print("{} arguments.".format(cnt))
    elif cnt == 1:
        print("{} argument:\n{}: {}".format(cnt, cnt, argv[1]))
    else:
        print("{} arguments:".format(cnt))
        for i in range(cnt):
            print("{}: {}".format(i + 1, argv[i + 1]))
