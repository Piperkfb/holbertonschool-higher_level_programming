
#!/usr/bin/python3
"""Appends"""


def append_write(filename="", text=""):
    """Write something new"""
    with open(filename, 'w', encoding="utf-8") as Filez:
        return Filez.append(text, end="")
