'''
Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra 'A';
Em que posição ela aparece a primeira vez;
Em que posição ela apareceu a última vez.
'''
# lendo a frase do usuário
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'Quantas vezes aparece a letra a: {frase.count('A')}')
print(f'Em que posição ela aparece primeiro: {frase.find('A') + 1}')
print(f'Em que posição ela aparece por último: {frase.rfind('A') + 1}')