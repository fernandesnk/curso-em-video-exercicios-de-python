#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 == n2:
  print(f'Não existe vamor maior, os dois são iguais!')
elif n1 > n2:
  print(f'{n1} é MAIOR que {n2}!')
else:
  print(f'{n2} é MAIOR que {n1}!')