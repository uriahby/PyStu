from math import *
import re


def weight(r, h):
    return round(pi * (r ** 2) * h / 1000, 2)

def expr():
    txt3 = "pink flag red flag black flag blue flag green flag red flag"
    pattern = "red flag|blue flag"
    print(re.findall(pattern, txt3))


def main():
#    print(weight(30, 60))
    print(2**38)


if __name__ == "__main__":
    main()
