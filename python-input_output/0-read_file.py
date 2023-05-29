
#!/usr/bin/python3
"""Read my lips"""


def read_file(filename=""):
    """What does this say"""
    with open(filename, encoding="utf-8") as DaFile:

        print(DaFile.read())
