# # estrutura sequêncial
# numero1 = int(input('Insira um valor: '))
# numero2 = int(input('Insira outro valor: '))

# if numero1 > numero2:
#     print(f'O {numero1} é maior que {numero2}')
# else:
#     print(f'O {numero1} é menor que {numero2}')

# tempo = int(input('Quantos anos tem seu carro? '))

# if tempo <= 3:
#     print('Seu carro é novo!')
# else:
#     print('Seu carro é velho!')
# print('FIM!')

# # versão simplificada
# tempo = int(input('Quantos anos tem seu carro? '))
# print(f'carro novo'if tempo<=3 else'carro velho')
# print('FIM!')

# nome = str(input('Qual é o seu nome? '))

# if nome == 'Nycollas':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal!')
# print(f'Bom dia, {nome}!')

# só if = condição simples, com else = condição composta.

n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi: {m}')
if m >= 7:
    print('Sua nota foi ótima, PARABENS!')
else:
    print('Sua nota fuim ruim, ESTUDE MAIS!')
