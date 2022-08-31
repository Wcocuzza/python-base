#!/usr/bin/env python3

import time
import logging

log = logging.Logger("errors")

# EAFP - Eae to ask forgivennes than permission

# def try_to_open_a_file(filepath, retry=1):
#     """Tries to open a file, if error, retries n times"""
#     for attempt in range(1, retry + 1):
#         try:
#             return open(filepath).readlines()
#         except FileNotFoundError as e:
#             log.error("[Error]: %s", e)
#             time.sleep(2)
#         else:
#             print("Sucesso!")
#         finally:
#             print("Execute isso sempre!")
#     return []

# Usando recursão
def try_to_open_a_file(filepath, retry=1):
    """Tries to open a file, if error, retries n times"""
    if retry > 999:
        raise ValueError("Rety cannot be above 999")
    try:
        return open(filepath).readlines()
    except FileNotFoundError as e:
        log.error("[Error]: %s", e)
        time.sleep(2)
        if retry > 1:
            return try_to_open_a_file(filepath, retry=retry - 1)
    else:
        print("Sucesso!")
    finally:
        print("Execute isso sempre!")
    return []

for line in try_to_open_a_file("names.txt", 5):
    print(line)