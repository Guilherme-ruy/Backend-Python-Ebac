# -- TESTES com RANDOM -- 
import random

print(random.randint(1, 10))

# Usando variavel e atribuindo um "choice"
escolha = random.choice(['pedra', 'papel', 'tesoura'])
print("Jokenpô:",escolha)


# -- TESTES com MATH --
import math

potencia = math.pow(2, 3)
print("Potência de 2^3:",potencia)

inteiro_acima = math.ceil(2.5)
print("Inteiro acima de 2.5:",inteiro_acima)


# -- TESTES com TIME --
import time

for i in range(4):
    print("Dormindo em:",i)
    time.sleep(1)
    

# -- TESTES com DATETIME --
import datetime as dt

data_agora = dt.datetime()
print("Data de sono:",data_agora)