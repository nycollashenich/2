'''
Crie um programa que leia um número inteiro e mostre na tela se ele
é par ou ímpar.
'''
print('PAR ou ÍMPAR')
num = int(input('Digite o número: '))
resultado = num % 2
if resultado == 0: 
    print('O número é PAR!')
else:
    print('O número é ÍMPAR!')

