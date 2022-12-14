#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input('Informe o nome da tua cidade: ')).lower().split()
if 'santo' in cidade[0]:
    print('O nome de sua cidade começa com Santo!') 
else:
    print('O nome da sua cidade NÃO começa com Santo!')