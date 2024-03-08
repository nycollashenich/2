'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço
a pagar, sando que o carro custa R$ 60 por dia e R$0,15 por Km rodado.
'''
print('ALUGUEIS DE CARROS')
dias_usados = int(input('Quantos dias o carro foi usado? '))
km_rodados = int(input('Quantos km foram rodados? '))

custo_dia = dias_usados * 60
custo_km = km_rodados * 0.15

preco_a_pagar = custo_dia + custo_km

print(f'O preço a pagar será de R${preco_a_pagar:,.2f} por {dias_usados} dias usados e {km_rodados}km rodados')