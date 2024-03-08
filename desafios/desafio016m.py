'''
crie um programa que leia aum número Real qualquer pelo teclado
e mostre na tela a sua porção inteira.
'''
# sessão import
from math import floor, trunc

#floor = arredonda para baixo
num = float(input('Digite um número com ".": '))
print(floor(num))

#trunc = a partir da virgula tira tudo
num2 = float(input('Digite um número com ".": '))
print(trunc(num2))

#sem modulos. Com int
num3 = float(input('Digite um valor: '))
print(f'O valor é {int(num3)}')
