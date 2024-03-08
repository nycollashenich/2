'''
Crie um programa que leia o nome de uma pessoa
e diga se ela tem silva no nome.
'''
nome = input('Digite seu nome: ').strip()
silva = 'silva' in nome.lower()

print('O nome tem "Silva"?', silva)
