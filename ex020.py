# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
a1 = str(input('Digite o nome do 1º aluno(a):'))
a2 = str(input('Digite o nome do 2º aluno(a):'))
a3 = str(input('Digite o nome do 3º aluno(a):'))
a4 = str(input('Digite o nome do 4º aluno(a):'))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentação será {lista}')