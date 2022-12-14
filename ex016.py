# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''opcao 1
num = float(input('Digite um número: '))
print(int(num))'''
from math import trunc
num = float(input('Digite um número: '))
print(trunc(num))

