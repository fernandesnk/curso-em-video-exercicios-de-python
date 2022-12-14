#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Digite seu nome completo: ')).lower()
if 'silva' in nome:
    print('Você possui Silva em seu nome!')
else:
    print('Você NÃO possui Silva em seu nome!')