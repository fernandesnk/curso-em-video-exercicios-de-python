#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
a1 = str(input('Digite o nome do 1º aluno(a):'))
a2 = str(input('Digite o nome do 2º aluno(a):'))
a3 = str(input('Digite o nome do 3º aluno(a):'))
a4 = str(input('Digite o nome do 4º aluno(a):'))
lista = [a1, a2, a3, a4]
sorteado = choice(lista)
print(sorteado)
