from math import *
import re


def weight(r, h):
    return round(pi * (r ** 2) * h / 1000, 2)


def expr():
    txt3 = "pink flag red flag black flag blue flag green flag red flag"
    pattern = "red flag|blue flag"
    print(re.findall(pattern, txt3))


def is_repeated(strn):
    i = 1
    ch_str = strn[0:1]
    while len(ch_str) <= len(strn) // 2:
        if ch_str * (len(strn) // len(ch_str)) == strn:
            return len(strn) // len(ch_str)

        i += 1
        ch_str = strn[0:i]
    return False


def count_vowels(txt):
    count = 0
    lst = ["a", "e", "i", "u", "o"]
    for l in lst:
        count += txt.count(l)
    return count


def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        try:
            return num1 / num2
        except Exception:
            return "Can't divide by 0!"


def main():
    #   print(weight(30, 60))
    #   print(2 ** 38)
    print(count_vowels("iuoqhroiubevfoib"))


if __name__ == "__main__":
    main()
