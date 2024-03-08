'''
faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo, calcule e mostre
o comprimento da hipotenusa.
'''
import math
print('TRIANGULOS')

#sem importação

print('='*19)
cateto_oposto0 = float(input('Informe o valor do cateto oposto: '))
cateto_adjacente0 = float(input('Informe o valor do cateto Adjacente: '))

hipotenusa = (cateto_oposto0 **2 + cateto_adjacente0 **2)**(1/2)
print(f'O valor da Hipotenusa é: {hipotenusa:.2f}')
print('='*19)


#com importação = math
#de forma mais simples = math.hypot : formula inteira
print('='*19)
co = float(input('Insera o valor do cateto Oposto:'))
ca = float(input('Insira o valor do cateto Adjacente: '))
hip = math.hypot(co,ca)
print(f'{hip:.2f}')


#junção da importação com sqrt
print('='*19)
cateto_oposto = float(input('Digite o cateto Oposto: '))
cateto_adjacente = float(input('Digite o cateto Adjacente: '))

comprimento_hipotenusa = math.sqrt(cateto_oposto **2 + cateto_adjacente **2)

print(f'{comprimento_hipotenusa:.2f}')
print('='*19)