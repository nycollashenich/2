"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre
a sua  média.
"""
nome_aluno = input('Digite o nome do aluno: ')
primeira_nota = input('Digite a primeira nota: ')
segunda_nota = input('Digite a segunda nota: ')

nota1_int = int(primeira_nota)
nota2_int = int(segunda_nota)

nota_media = (nota1_int + nota2_int) / 2
print(f'A medía das notas (primeira nota {nota1_int}) e (segunda nota {nota2_int}) é {nota_media}')
