#from doce import pudim = importa so as que eu quiser.
#import bebida = importa todas as funcionalidades de um modulo.

'''
math
   ceil = arredondar para cima 
   floor = arredondar para baixo                     "ou utilizar :.2f" 
   trunc = elimar da virgular para frente                                            
   pow = potencia troca por ** 
   sqrt = raiz quadrada
   factorial = fatorial
''apens raiz quadrada : from / math / import / sqrl 
'''
from math import sqrt, floor, ceil # Aqui importei somente sqrt, floor, ceil! APENAS ELES
#import math = para todos

num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é {(raiz)}')


num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é {floor(raiz)}')

print('='*20)

import random
num = random.random() # números aleatórios.
print(num)

import random
num = random.randint(1, 50) # números aleatórios INTEIROS(colocar entre (parenteses))
print(num)

nome1 = 'Ny'
nome2 = 'Ju'
sorteio = sorted(nome1, nome2)
print (sorteio)
