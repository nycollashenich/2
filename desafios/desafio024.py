'''
Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "Santo".
'''
# lendo a cidade do usuário
cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')

'''
strip para remover os espaços se o usuário digitar
cidade [:5], conta do primeiro (s) caractere até utimo (o)
upper = joga tudo para a maiusculo
'''
