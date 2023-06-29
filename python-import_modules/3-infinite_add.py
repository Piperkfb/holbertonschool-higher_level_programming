#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    cnt = len(argv) - 1
    answ = 0
    for i in range(cnt):
        num = int(argv[i + 1])
        answ += num
    print("{}".format(answ))
