"""
Iterando strings com while
"""

nome = 'Nelson Santos Junior'
novo_nome = ''
indice = 0
while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    indice += 1
    

print(novo_nome)