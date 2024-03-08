# CADEIA DE CARACTERES = string
nome = 'Nycollas Henrique Henich'

# FATIAMENTO
print(f'[Fatiamento]:', nome[7:14:2])# i : m : f = inicio da str, ate onde quero chegar, pulando
# :0:2 = i = omito

# ANÁLISE
print(f'LEN: ',len(nome)) # comprimento da frase = len/conta os caracteres
print(f'COUNT: ',nome.count('n',0,24)) # count = conta quantas letras repetidas
print(f'FIND: ',nome.find('N')) # quando os caracteres começam! / se receber -1 ela nao existe!
print(f'IN: ','llas' in nome) # exite llas em nome: volta true! ou sim

# TRANSFORMAÇÃO
print(f'REPLACE: ', nome.replace('Nycollas', 'lindao')) # replace = substitue Nycollas, por lindao! (de forma sec)
print(f'UPPER: ', nome.upper()) # deixa tudo maisculo
print(f'LOWER: ', nome.lower()) # deixa tudo minusculo
print(f'CAPITALIZE: ', nome.capitalize()) # pegar um str inteira e jogar minusculo, menos a primeira
print(f'TITLE: ', nome.title()) # a cada espaço deixa a letra maiuscula
print(f'STRIP: ', nome.strip()) # remove todos os espaços inuteis no inico e no fim, menos no meio
print(f'RSTRIP: ', nome.rstrip()) # r = direita, remove somentos espaços da strg da direita
print(f'LSTRIP: ', nome.lstrip()) # l = esquerda, remove somentos espaços da strg da esquerda

# DIVISÃO
print(f'SPLIT: ', nome.split()) # onde tiver espaços ele cria um divisão = refaz os numeros dos caracteres
#separando eles em espaços! ou seja, divide uma strg, cria uma lista eles vão ter novas numeraçoes!

# JUNÇÃO
print(f'JOIN: ', ' '.join(nome)) # coloca caracteres entre as letras! esse é zica


#como escrever um texto grande?
#colocar """ = três aspas. Ex:
'''printrint("""To run the Python script you have open on the editor, select the Run Python File 
in Terminal play button in the top-right of the editor. 
There are also additional ways you can iteratively run snippets of your 
Python code within VS Code: Select one or more lines, then 
press Shift+Enter or right-click and select Run Selection/Line in Python Terminal.""")'''


# como mudar a frase utilizando replace, desse modo: fazendo uma atribuição
nome1 = 'O Nycollas é feio'
nome1 = nome1.replace('feio','lindo!')
print(nome1) 