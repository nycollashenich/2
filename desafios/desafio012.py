'''
Faça um algoritimo que leia o preço de um produto e mostre 
seu novo preço, com 5% de desconto.
'''
print('PRODUTO COM 5% DE DESCONTO!')
preco_produto = float(input('Digite o preço do produto: R$ '))
valor_final = preco_produto - (preco_produto * 5/100)
print(f'O valor final do produto com 5% de desconto é de: R${valor_final:,.2f}')