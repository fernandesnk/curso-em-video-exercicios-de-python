# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''opcao 1
co = int(input('Informe o valor do cateto oposto: '))
ca = int(input('Informe o valor do cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print(f'Em um triãngulo cujo os catetos são {co} e {ca}, a hipotenusa vale {hip}.')'''

'''opcao 2
from math import hypot
co = int(input('Informe o valor do cateto oposto: '))
ca = int(input('Informe o valor do cateto adjacente: '))
print(f'Em um triãngulo cujo os catetos são {co} e {ca} o valor da hipotenusa é {hypot(co, ca)}')'''
