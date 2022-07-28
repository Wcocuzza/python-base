#!/usr/bin/env python

"""Exibe relatório de crianças por atividade.

Impimir a lista de crianças agrupadas por sala que frequentam cada uma das
atividades.
"""
__version__ = "0.1.2"

escola = {
    "turmas": {
        "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
        "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
    },
    "cursos_extras": {
        "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
        "Música": ["Erik", "Carlos", "Maria"],
        "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
    },
}

for curso in escola["cursos_extras"]:

    print(f"Alunos da atividade de {curso}")
    print("-" * 40)
    
    atividade_sala1 = set(escola["turmas"]["sala1"]) & set(escola["cursos_extras"][curso])
    atividade_sala2 = set(escola["turmas"]["sala2"]) & set(escola["cursos_extras"][curso])

    print(f"Sala1 {atividade_sala1}")
    print(F"Sala2 {atividade_sala2}")
    print()
    print("*" * 40)

