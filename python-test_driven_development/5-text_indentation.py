#!/usr/bin/python3
"""prints adouble new line at points: """

def text_indentation(text):
    """As seen on TV """

    if type(text) != str:
        raise TypeError("text must be a string")

    sen = ""
    i = 0
    while i < len(text):
        if text[i] != "." and text[i] != "?" and text[i] != ":":
            sen += text[i]
        else:
            sen += text [i]
            print(sen)
            print()
            sen = ""
            while i < (len(text) - 1) and text[i+1] == "":
                i += 1
        i += 1
    print(sen, end="")
