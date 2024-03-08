'''
Sorteio da ordem de apresentação. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
from random import shuffle #shuffle embaralhar a lista

nome1 = input('Nome do primerio grupo: ')
nome2 = input('Nome do segundo grupo: ')
nome3 = input('Nome do terceiro grupo: ')
nome4 = input('Nome do quarto grupo: ')

#ordem do sorteio
lista_grupos = [nome1, nome2, nome3, nome4]
shuffle(lista_grupos) 
print(f'A ordem é: {lista_grupos}') 