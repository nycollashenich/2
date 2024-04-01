# file = open('TESLA - atividade.txt','r')

# print(file)

# open('r', 'w', 'a')
# file.read() = leitura
# write = escrever
# close = fechar


with open('arquivo_origem.txt','r') as arquivo_origem:
    conteudo = arquivo_origem.read()

print('Conteúdo do arquivo origem: ')
print(conteudo)

with open('arquivo_destino.txt', 'w') as arquivo_destino:
    arquivo_destino.write(conteudo)

print('Conteúdo do arquivo de origem foi copiado para o arquivo de destino.')
