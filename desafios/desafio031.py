'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 po Km para viagens de ate 200km
e R$0,45 para viajens mais longas.
'''
print('VIAGEM')

# lendo a distância
distancia = float(input('Qual a distância da sua viagem? '))

print('='*30)
print('CURTA - Viagem até 200km: R$0,50\nLONGA - A partir: R$0,45')
print('='*30)

preco_curta = distancia * 0.50
preco_longa = distancia * 0.45

if distancia <= 200:
    print(f'CURTA - O preço da sua viagem é: R${preco_curta:.2f}')
else:
    print(f'LONGA - O preço da sua viagem é: R${preco_longa:.2f} ')