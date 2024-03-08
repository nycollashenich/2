
'''
Escreva um programa que converta uma temperatura digitando em graus Celsius
e converta para graus Fahrenheit
'''
print('TRANSFORMANDO C° em F°!')
temperatura_em_celsius = float(input('Informe a temperatura em C°: '))

celsius_para_f = (temperatura_em_celsius * 1.8) + 32
print(f'{temperatura_em_celsius}C° em F°: {celsius_para_f}')