"""Este modulo serve apenas de anotação"""

# Definição de função ou atribuição
# Assinatura + type hints
# Documentação / docstring
# Codigo
# Valor de retorno





def nome_da_funcao(a: int, b: int, c: int) -> int:
    """Esta função soma a, b e c.

    Use esta função quando quiser a + b + c

    >>> nome_da_funcao(1, 2, 3)
    6
    """
    resultado = a + b + c
    return resultado

# Passagem de argumentos posicionais
valor = nome_da_funcao(1, 2, 3)

# Passagem de argumentos nomeados
valor = nome_da_funcao(a=1, b=2, c=3)

# Passagem de argumentos mistos
# Argumentos posicionais vem antes dos nomeados
valor = nome_da_funcao(1, b=2, c=3)

# Funcao com muitos argumentos
valor = nome_da_funcao(
    1,
    2, 
    c=3,
)

def outra_funcao(a, b, c):
    """docstring"""
    return a * 2, b * 2, c * 2

valor1, valor2, valor3 = outra_funcao(1, 2, 3)

valor1, *resto = outra_funcao(1, 2, 3)

# Passagem de argumentos com desempacotamento
def soma(n1, n2):
    """Soma dois numeros"""
    return n1 + n2

# Normal
print(soma(10, 20))

# Argumentos em sequencia
args = (10, 20) # tuple, list, str
print(soma(args[0], args[1])) # Explicito
print(soma(*args)) # desempacotando

# Argumentos dict / nomeados
args = {"n2": 20, "n1": 40} # dict, hashmap
print(soma(n1=args["n1"], n2=args["n2"])) # Explicito
print(soma(**args)) # Desempacotando argumentos nomeados

lista_de_valores_para_somar = [
    {"n2": 20, "n1": 40},
    {"n2": 20, "n1": 50},
    {"n2": 20, "n1": 60},
    (5, 10),
    [8, 13],
]

for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print(soma(**item))
    else:
        print(soma(*item))

        