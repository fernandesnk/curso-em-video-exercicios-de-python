# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).lower()
num_ocorrencias = frase.count('a')
sem_espaco = ''.join(frase.split())
primeira_ocorrencia = sem_espaco.find('a') #find identifica a primeira ocorrência do valor especificado
ultima_ocorrencia = sem_espaco.rfind('a') # rfind identifica a última ocorrência, já que começa a -leitura' pelo lado direito
print(f'A letra "a" aparece {num_ocorrencias} vezes na frase {frase} ')
print(f'A primeira ocorrência da letra "a" é no índice {primeira_ocorrencia + 1}') # acrescentar +1 pq o índice começa do zero, mas no cotidiano começamos a contar do 1.
print(f'A última ocorrência da letra "a" é no índice {ultima_ocorrencia + 1}')


