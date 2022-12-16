#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
contador = 0
for x in range (1,7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        contador += 1
        soma += num
print(f'Dos 6 números digitados {contador} são pares, e o resultado da soma deles é {soma}!')
