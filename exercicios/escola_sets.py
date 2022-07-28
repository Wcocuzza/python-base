#!/usr/bin/env python

"""Exibe relatório de crianças por atividade.

Impimir a lista de crianças agrupadas por sala que frequentam cada uma das
atividades.
"""
__version__ = "0.1.1"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca)
]

for nome_atividade, atividade in  atividades:
    print(f"Alunos da atividade de {nome_atividade}")
    print("-" * 40)
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    print(f"{nome_atividade} da sala1 {atividade_sala1}")
    print(F"{nome_atividade} da sala2 {atividade_sala2}")
    print()
    print("*" * 40)

