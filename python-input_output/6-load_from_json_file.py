#!/usr/bin/python3
"""I'm so tired"""


def load_from_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return (json.load(f))
