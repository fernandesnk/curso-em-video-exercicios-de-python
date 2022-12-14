# Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
maiuscula = nome.upper()
minuscula = nome.lower()
total_letras = len(''.join(nome.split()))
total_fname = len((nome.split())[0])
print(f'{maiuscula}')
print(f'{minuscula}')
print(f'O teu nome completo possui {total_letras} letras! ')
print(f'O teu primeiro nome possui o total de {total_fname} letras!')