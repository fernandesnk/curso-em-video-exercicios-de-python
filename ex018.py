#  Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
angulo = float(input('Informe o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O seno, cosseno e tangente do ângulo {angulo} são {seno:,.2f}, {cosseno:,.2} e {tangente:,.2f}, respectivamente.')
