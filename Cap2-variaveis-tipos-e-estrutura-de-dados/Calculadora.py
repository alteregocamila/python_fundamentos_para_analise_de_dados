from time import sleep

print(10*'*', 'PYTHON CALCULATOR', 10*'*')
sleep(1)

print('\nSelecione no menu a seguir a operação desejada.')
sleep(1)

print('\n1 - soma', '\n2 - subtração', '\n3 - multiplicação','\n4 - divisão')
sleep(1)

operator = int(input('\nOperação (1/2/3/4): '))
sleep(1)

if operator > 4:
    print('\nOpção inválida!')
    exit()
else:
    lista = []
    for i in range(1, 3):
        num = float(input('\nDigite um número: '))
        lista.append(num)

num1 = lista[0]
num2 = lista[1]

sleep(1)

if operator == 1:
    soma = num1 + num2
    print('\nA soma de {} com {} é {}.\n'.format(num1, num2, soma))
elif operator == 2:
    sub = num1 - num2
    print(('\nA subtração de {} de {} é {}.\n'.format(num2, num1, sub)))
elif operator == 3:
    mult = num1 * num2
    print(('\nA multiplicação de {} por {} é {}.\n'.format(num1, num2, mult)))
else:
    div = num1 / num2
    print(('\nA divisão de {} por {} é {}.\n'.format(num1, num2, div)))
    sleep(1)

print(10*'*', 'PYTHON CALCULATOR', 10*'*')

