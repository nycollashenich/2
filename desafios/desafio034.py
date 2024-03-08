'''
Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = int(input('Insira seu salário: R$ '))
if salario > 1251:
    print(f'Você irá receber um aumento de 10%: R${(salario * 10/100) + salario:.2f}')
if salario <= 1250:
    print(f'Você recebera um aumento de 15%: R${(salario * 15/100) + salario:.2f}')