#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "<Title>"
tag: <sobre>
text:
um texto qualquer que fala sobre <tag: <sobre>>

$notes.py read tag
...
...
"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

cmds = ("read", "new")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage!")
    print(f"you must specify subcommand {cmds}")
    sys.exit(1)


if arguments[0] not in cmds:
    print(f"Invalid command: {arguments[0]}")

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"tile: {title}")
            print(f"text: {text}")
            print("_ * 30")
            print()

if arguments[0] == "new":
    try:
        title = arguments[1]
        text = [
        f"{title}\n",
        input("tag: ").strip(),
        input("text:\n").strip()
    ]
    except IndexError as e:
        print(str(e))
    
    # \t - tsv

try:
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
except PermissionError as e:
    print(str(e))
    sys.exit(1)