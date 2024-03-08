'''
Crie um algoritimo que leia um número e mostre o seu dobro, triplo
e raiz quadrada.
'''
num_int = input('Digite um número: ')

numero_int = int(num_int)
dobro = (numero_int * 2)
triplo = (numero_int * 3)
raiz_quadrada = (numero_int ** (1/2))

print(f'O dobro do número digitado é {dobro}')
print(f'O triplo do número digitado é {triplo}')
print(f'A raíz do número digitado é {raiz_quadrada:.0f}')
