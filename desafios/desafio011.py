'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule
a sua área e quantidade de tinta necessária para pintá-la, sabedno que cada litro
pinta uma área de 2m².
'''

parede_largura = float(input('Digite a largura da parede: '))
parede_altura = float(input('Digite a altura da parede: '))

area = (parede_largura * parede_altura)
print(f'A área da parede é: {area}m²')

print('='*20)
print('Quantidade de tinta!')
quant_tinta = area / 2
print('='*20)

print(f'A quantidade de tinta necessária para pintar a parede é: {quant_tinta:.2f}l')