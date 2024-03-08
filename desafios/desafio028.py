'''
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido
pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random
from time import sleep

print('JOGO DA ADIVINHAÇÃO')
print('--=--'* 20)
print('EU, computador ESTOU PENSANDO EM UM NÚMERO de 0 a 5...')
print('SERÁ QUE VOCÊ CONSEGUE ADVINHAR em QUAL estou PENSANDO?')
print('--=--'* 20)

# coletando dados do usuário
resposta = int(input('DIGITE O VALOR ESCOLHIDO... '))
print(f'O NÚMERO ESCOLHIDO FOI: {resposta}')
print('--=--'* 20)
print('PROCESSANDO...')
sleep(3)

# escolha do computador
escolha = random.randint(0, 5) # random dos números

if escolha == resposta:
    print(f'PARABÉNS, você adivinhou!\nEu pensei no número: {escolha}')
else:
    print(f'RESPOSTA ERRADA, TENTE outra vez!\nEu pensei no número: {escolha}')