# Tipos básicos de variáveis

# Variável inteira (int)
numero_inteiro = 10
print("Número inteiro:", numero_inteiro)

# Variável de ponto flutuante (float)
numero_decimal = 10.5
print("Número decimal:", numero_decimal)

# Variável de string (str)
texto = "Olá, mundo!"
print("Texto:", texto)

# Variável booleana (bool)
verdadeiro_ou_falso = True
print("Valor booleano:", verdadeiro_ou_falso)

# Lista
lista_frutas = ["maçã", "banana", "cereja"]
print("Lista de frutas:", lista_frutas)

# Tupla
coordenadas = (10, 20)
print("Coordenadas:", coordenadas)

# Conjunto
conjunto_numeros = {1, 2, 3, 4, 5}
print("Conjunto de números:", conjunto_numeros)

# Dicionário
dicionario_pessoa = {"nome": "João", "idade": 25}
print("Dicionário de pessoa:", dicionario_pessoa)

# Variável none (NoneType)
variavel_vazia = None
print("Variável None:", variavel_vazia)

# Exemplo de variáveis locais e globais
x_global = 10  # Variável global

def minha_funcao():
    x_local = 5  # Variável local
    print("x local dentro da função:", x_local)
    print("x global dentro da função:", x_global)

minha_funcao()
print("x global fora da função:", x_global)

# Variáveis compostas e operações
soma = numero_inteiro + numero_decimal
print("Soma de int e float:", soma)

concatenacao = texto + " Como vai?"
print("Concatenação de strings:", concatenacao)

media_lista = sum(lista_frutas) / len(lista_frutas) if lista_frutas else 0
print("Média da lista de frutas (comprimento das strings):", media_lista)

# Entrada e saída de dados
nome_usuario = input("Digite seu nome: ")
idade_usuario = int(input("Digite sua idade: "))
print(f"Olá, {nome_usuario}! Você tem {idade_usuario} anos.")

# Exemplo de uso de lista para armazenar notas e calcular a média
notas = []
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media_notas = sum(notas) / len(notas)
print(f"A média das notas é: {media_notas:.2f}")