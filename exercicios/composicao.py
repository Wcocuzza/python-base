"""Imprime apenas os nomes iniciados com a letra B"""

names = [
    "Wallace",
    "Bruno",
    "Daniel",
    "Diego",
    "Butura",
    "Luthi",
    "Natalia",
]

# def starts_with_b(text):
#     return text[0].lower() == "b"

print(*list(filter(lambda text: text[0].lower() == "d", names)), sep="\n")