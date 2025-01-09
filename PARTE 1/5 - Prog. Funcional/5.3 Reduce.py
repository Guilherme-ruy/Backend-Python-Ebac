'''
Aplica uma função a todos os elemento de uma coleção,
dois a dois, e retorna **apenas** um elemento.
'''

# variavel = reduce(função, coleção)
from functools import reduce


# Exemplo 1
numeros = [1, 2, 3]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)

# Exemplo 2
def maior_entre(primeiro: int, segundo: int) -> int:
    return primeiro if primeiro >= segundo else segundo


primeiro = 11
segundo = 11

print(maior_entre(primeiro=primeiro, segundo=segundo))