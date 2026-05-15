# if / elif      /else
# se / se não se / se não

saida = str(input('Você deseja sair? [S/N]: ')).upper()

if saida == "S":
    print('Você saiu do sistema!')
elif saida == 'N':
    print('Você continua no sistema!')
else:
    print('Somnte S ou N')