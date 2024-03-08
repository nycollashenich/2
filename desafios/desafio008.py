"""
Escreva um programa que leia um valor e metros e o exiba convertido
em centimetros e milimetros.
"""
print('VOU TRANSFORMAR METROS EM km, hm, dam, dm, cm, mm!')

numero_em_metros = float(input('Digite seu número em metros: '))

transformacao_dam = (numero_em_metros / 10)
transformacao_hm = (transformacao_dam / 10)
transformacao_km = (transformacao_hm / 10)

transformacao_dm = (numero_em_metros * 10)
transformacao_cm = (transformacao_dm * 10)
transformacao_mm = (transformacao_cm * 10)

print(f'Transformando em km: {transformacao_km}km')
print(f'Transformando em hm: {transformacao_hm}hm')
print(f'Transformando em dam: {transformacao_dam}dam')
print(f'Transformando em dm: {transformacao_dm}dm')
print(f'Transformando em cm: {transformacao_cm}cm')
print(f'Transformando em mm: {transformacao_mm}mm')