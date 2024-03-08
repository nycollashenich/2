'''
Faça um programa que leia o nome do usuário completo
mostrando em seguida o primeiro nome e o último nome 
separadamente.

Ex: Ana Maria de Souza
primeiro: Ana
últmo: Souza
'''
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print('Primeiro nome:',nome[0])
print('Último nome:',nome[len(nome)- 1])
