'''
Crie um programa que, leia o nome completo de uma pessoa e
mostre:

O nome com todas as letras maiúsculas;
O nome com todas as letras minúsculas;
Quantas letras tem ao todo, sem contar os espaços;
Quantas letras tem o primeiro nome.

'''

# lendo nome do usuário
nome_entrada = str(input('Informe seu nome: ')).strip()

# Transformando em maiúsculo
print('Maiúscula:',nome_entrada.upper())

# Transformando em letras minúsculas
print('Minúscula:',nome_entrada.lower())

# Número de letras sem os espaço
print('Quantas letras tem seu nome inteiro:',len(nome_entrada) - nome_entrada.count(' ')) 
# Colocar o - para remover os ' ' espaços.

# Primeiro nome
primeiro_nome = nome_entrada
primeiro_nome = nome_entrada.split()
print(f'Seu primeiro nome tem: {len(primeiro_nome[0])} letras.')
# Para saber o primerio nome é so numerar, colocando o numero da lista
# Posso selecionar a lista, e a letra que eu quero dentro dela Ex: [0][2]


# Outro modo de contas as letras:
print(f'2° Seu primerio nome tem: {nome_entrada.find(' ')} letras.')