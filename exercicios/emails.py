
from genericpath import exists
import os
from re import template
import sys

arguments = sys.argv[1:]
if not arguments:
    print("Informe a base de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

clientes = []
for line in open(filepath):
    name, email = line.split(",")
    # TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "nome": name, 
            "produto": "caneta", 
            "texto": "Escrever muito bem",
            "link": "https://google.com",
            "quantidade": 1,
            "preco": 5.9,
        }
    )
    print("-" * 50)