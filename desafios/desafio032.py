'''
Faça um programa que um ano qualquer e mostre se ele é bissexto.
'''
from datetime import date

print('DESCUBRA SE O ANO É BISSEXTO')
ano = int(input('Qual ano deseja saber? '))

if ano == 0:
    ano = date.today().year # ano da máquina, em qualquer pc.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano}, é um ano bissexto!')
else:
    print(f'{ano}, não é um ano bissexto!')