'''
Faça um algortimo que leia o salário de um funcionário e mostre 
seu novo salário, com 15% de aumento
'''
print('AUMENTO DE 15% NO SALÁRIO')
nome_funcionario = input('Nome do funcionário: ')
salario_funcionario = float(input(f'Salário de {nome_funcionario}: '))

print('AUMENTO DE 15%!')
calculo_porcentegem = salario_funcionario * 15/100
aumento = salario_funcionario + calculo_porcentegem

print(f'O aumento no salário de {nome_funcionario} é R${calculo_porcentegem}')
print(f'O valor futuro do salário é de: R${aumento}')