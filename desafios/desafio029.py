'''
Escreva um programa ue leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 a cada km acima do limite.
'''
print('RADAR DE VELOCIDADE')
print('Valor da multa: R$7,00 a cada km ultrapassado')

velocidade_padrao = 80
velocidade_passou = float(input('Insira a velocidade do carro: '))
multa = (velocidade_passou - velocidade_padrao) * 7

if velocidade_passou > velocidade_padrao:
    print(f'Você ultrapassou a velocidade permitida de 80km/h! com {velocidade_passou}km\nO valor dá multa é: R${multa}')
else:
    print('Siga em frente! Está dentro da velocidade permitida.')
