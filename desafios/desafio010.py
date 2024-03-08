'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode compra
'''
print('TRANSFORMANDO REAIS EM DÓLAR!')

brl = float(input('Quantos R$ você tem? '))
usd = 4.97
cambio = (brl / usd)
print(f'Cotação DÓLAR: {usd}')

print(f'Você tem R${brl}\nTransformado em dólar: US${cambio:.2f}')