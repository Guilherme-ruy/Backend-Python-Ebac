# -- variaveis -- 
recebimento_1 = 10.50
recebimento_2 = 20.50
recebimento_3 = 30.50
recebimento_4 = 40.50

#concatenação
recebimento_total = recebimento_1 + recebimento_2 + recebimento_3 + recebimento_4

#passando para lista
recebimento_total_lista = [recebimento_1, recebimento_2, recebimento_3, recebimento_4, recebimento_total]
#recebimento_total_lista_tipo2 = list(recimento_total) | erro pois recebimento_total é float... e não pode ser list

print("Recebimento total:",recebimento_total)
print("Tipo do recebimento total:",type(recebimento_total))

#fatiamento fixo
print("Valor 2º Recebimento", recebimento_total_lista[1])

#fatiamento dinamico
print("Valor 2º e 3º Recebimento", recebimento_total_lista[1:3])

#inclusão
recebimento_total_lista.append(50.50)

print("Recebimento total lista:",recebimento_total_lista)
#valor com inclusão Recebimento total lista: [10.5, 20.5, 30.5, 40.5, 102.0, 50.5]


usuarios = ["João", "Maria", "Pedro", "Ana"]
#resultado: ['João', 'Maria', 'Pedro', 'Ana']
print(usuarios)
print(type(usuarios))

#remover por posição da lista
usuarios.pop(2)
#resultado: ['João', 'Maria', 'Ana']
print(usuarios)

#remover por valores da lista
usuarios.remove("Maria")
#resultado: ['João', 'Ana']
print(usuarios)

#conversão
email = 'guilherme@ebac.com.br'
email_conversao = list(email)
print('email:', email)
print('email conversão:', email_conversao)