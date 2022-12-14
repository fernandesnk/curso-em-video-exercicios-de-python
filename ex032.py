# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
#Caso 1) É um número divisível por 4, mas não é divisível por 100.
#Caso 2) É um número divisível por 4, por 100 e por 400.
ano = int(input('Informe um ano e descubra se ele é bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO É bissexto!')
