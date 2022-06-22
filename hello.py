#!/usr/bin/env python3
"""Hello World Multi linguagem
Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=<Linguagem do Sistema>

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
#Metadados são declarados usando dunder
__version__ = "0.0.1"
__author__ = "Wallace Cocuzza"
__license__ = "MIT"

import os


current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
print(msg)
