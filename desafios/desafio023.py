'''
Faça um programa que leia um número de 0 a 9999 e mostre
na tela cada um dos dígitos separados.
Ex:
Digite um número: 1834
milhar: 1
centena: 8
dezena: 3
unidade: 4 
'''
# aqui é de modo matemático, não da para fazer por str!, quer dizer 
# até dám, mas não mostra valores pequenos.
numero = int(input('Insira um valor: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Análisando o número {numero}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
