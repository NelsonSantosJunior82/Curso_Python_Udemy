"""Calculadora com while"""


import time 

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite somente os operadores(+-/*): ')

    numeros_validos = True
    num_1_float = 0
    num_1_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_validos = '+-/*'

    if operador not in operadores_validos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')

    print('Calculando ... ')
    time.sleep(2)

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ',num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ',num_1_float - num_2_float)
    elif operador == '/':
         print(f'{num_1_float} / {num_2_float} = ',num_1_float / num_2_float)
    elif operador == '*':
         print(f'{num_1_float} * {num_2_float} = ',num_1_float * num_2_float)
    else:
        print('Opa! Tem algo errado!')
    
    sair = input('Quer sair: [s]im: ').lower().startswith('s')

    if sair is True:
        break

    
    