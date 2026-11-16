"""while/else"""
string = 'ValorQualquer' # String sem espaço

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ': # Checa se há espaço na string
        break

    print(letra)
    i += 1

else:
    print('Não encontrei espaço na string!')
print('Fora do While')