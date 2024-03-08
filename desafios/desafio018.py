'''
Faça um programa que leia um ângulo qualquer e mostre na
tela o valor do seno, cosseno e tanguente desse ângulo.
'''
from math import sin, cos, tan, radians

# lendo o ângulo do usuario
angulo_entrada = input('Informe o ângulo: ')
angulo = int(angulo_entrada)

# seno, cosseno e tangente
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

# resultado
print(f'SENO: {seno:.2f}, COSSENO: {cosseno:.2f} e TANGENTE: {tangente:.2f}')