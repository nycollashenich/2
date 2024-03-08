'''
Um professor quer sortear um dos seus 4 alunos para
apagar o quadro. Faça um programa que ajude ele, lendo
o nome deles e escrevendo o nome do escolhido.
'''
from random import choice

print('SORTEIO')

# lendo os nomes dos usuários
nome1 = input('Nome do primerio aluno: ')
nome2 = input('Nome do segundo aluno: ')
nome3 = input('Nome do terceiro aluno: ')
nome4 = input('Nome do quarto aluno: ')

# formula do sorteio
lista_alunos = [nome1, nome2, nome3, nome4] #[] = lista
escolhido = choice(lista_alunos) # random.choice = apenas uma escolha!

# resultado do sorteio
print(f'O sortudo da vez foi: {escolhido}')