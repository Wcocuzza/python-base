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

while True:
    
    if arguments[0] == "new":
        try:
            title = arguments[1]
        except IndexError:
            title = input("Informe o titulo: ").strip().title()
        
        text = [
            f"{title}",
            input("tag: ").strip(),
            input("text:\n").strip()
        ]
        # \t - tsv

    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Informe a tag: ").strip().lower()

        for line in open(filepath):
            title, tag, text = line.strip().split("\t")
            if tag.lower() == arg_tag:
                print(f"tile: {title}")
                print(f"text: {text}")
                print("_" * 30)
                print()

    try:
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")
    except PermissionError as e:
        print(str(e))
        sys.exit(1)
    
    stop = input("Deseja continuar? [N/y]: ").strip().lower()
    if stop != "y":
        break