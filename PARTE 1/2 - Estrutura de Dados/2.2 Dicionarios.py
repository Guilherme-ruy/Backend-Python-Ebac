brasil = {'capital': 'Brasilia', 'idioma': 'Portugues', 'populacao': 210000000}
print(brasil)
print(brasil['capital'], "com idioma",brasil['idioma'])
print(type(brasil))
#Não permite chaves duplicadas

nomes = {
    'Guilherme':{'idade': 18},
    'Joamir':{'idade': 48},
    'Lerme':{'idade': 19},
}
print(nomes)
print(nomes['Guilherme'])

#print(nomes['Joamir'[::-1]])
#result: KeyError: 'rimaoJ'

contacts = {
    '123@gmail.com': {'nome': 'João'},
    '2fa@gmail.com': {'nome': 'João'},
    'ccc@gmail.com': {'nome': 'João'},
    'azx@gmail.com': {'nome': 'João'},
    '432@gmail.com': {'nome': 'João'}
}

#COPY
contacts_2 = contacts.copy()

print(f'seus contatos atuais:{contacts}')


#CLEAR
contacts.clear()
print(f'seus contatos atuais após o clear:{contacts}')

print(f'seus contatos para backup:{contacts_2}')

print(id(contacts)) #
print(id(contacts_2)) #

print(contacts_2.values()) #[{'nome': 'João'}, {'nome': 'João'}, {'nome': 'João'}, {'nome': 'João'}, {'nome': 'João'}])


#OUTRA ESTRUTURA DE DICT
artigo = dict(
    autor = 'Guilherme',
    ano = 2024,
    curso = 'Ebac'
)
print(artigo)

artigo.update({'autor':'Guilherme', 'ano': 2028, 'curso':'Ebac 2'})
print(artigo)

chaves_artigo = artigo.keys()
valores_artigo = artigo.values()
print("chaves artigo:",chaves_artigo)
print("valores artigo:",valores_artigo)
print(artigo.items())
print(type(chaves_artigo))
print(type(valores_artigo))
