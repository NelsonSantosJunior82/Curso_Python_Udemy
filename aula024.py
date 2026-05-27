'''
OPERADORES IN E NOT IN

Strings são iteráveis
 0 1 2 3 4 5
 N e l s o n
-6-5-4-3-2-1
'''
'''
nome = 'Nelson'

print(nome[2])
print(nome[-3])
print('s' in nome)
print('a' not in nome)
'''
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')