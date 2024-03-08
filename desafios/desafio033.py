'''
Faça um programa que leia três números e mostre qual é o maior e qual 
é o menor.
'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
maior = num1
menor = num1
# valor menor
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

# valor maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num1:
    maior = num3

print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')
# prestar a atenção nos blocos