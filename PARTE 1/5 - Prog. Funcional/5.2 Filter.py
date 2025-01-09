'''
Aplica uma função lógica (que retorna um booleano) em todos os elementos de uma coleção
(`list`, `dict`, etc.) e retorna **apenas** aqueles que resultaram em verdadeiro (`True`).
'''

# Exemplo 1

# variavel = filter(função, coleção)

numeros = [1, 2, 3]

numeros_par = filter(lambda num: num % 2 == 0, numeros)

print(list(numeros_par))

# Exemplo 2

emails = ['andre.perez@gmail.com', 'andre.perez@live.com', 'andre.perez@yahoo.com']

emails_google = filter(lambda email: 'gmail' in email, emails)
...
print(list(emails_google))