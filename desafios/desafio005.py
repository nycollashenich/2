"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor
e seu antecessor.
"""
entrada = input('Digite um número: ')
num_int = int(entrada)
sucessor = num_int + 1
antecessor = num_int - 1

if sucessor:
    print(f'O SUCESSOR do número {num_int} é {sucessor}')
if antecessor:
        print(f'O ANTECESSOR do número {num_int} é {antecessor}')