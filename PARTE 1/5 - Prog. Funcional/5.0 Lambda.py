# LAMBDA - Funções anônimas

# Exemplo 1
extrair_provedor_email = lambda email: email.split(sep='@')[-1]

email = 'andre.perez@gmail.com'
print(email)

provedor_email = extrair_provedor_email(email)
print(provedor_email)

# Exemplo 2
soma = lambda x, y: x + y
print(soma(2, 3))

# Exemplo 3
numero_e_par = lambda numero: True if numero % 2 == 0 else False
numeros = range(0, 10)
for numero in numeros:
  if numero_e_par(numero) == True:
    print(f'O número {numero} é par!')

# Exemplo 4
def retorno(juros: float):
  return lambda investimento: investimento * (1 + juros)

retorno_5_porcento = retorno(juros=0.05)
retorno_10_porcento = retorno(juros=0.10)

valor_final = retorno_5_porcento(investimento=1000)
print(valor_final)

valor_final = retorno_10_porcento(investimento=1000)
print(valor_final)

anos = 15
valor_inicial = 1000
valor_final = valor_inicial

for ano in range(1, anos+1):
  valor_final = retorno_10_porcento(investimento=valor_final)

valor_final = round(valor_final, 2)
print(valor_final)