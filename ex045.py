#Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
jogador = str(input('Escolha pedra, papel ou tesoura: '))
computador = choice(['pedra', 'papel', 'tesoura'])
if jogador == computador:
  print(f'Você escolheu {jogador} e o computador {computador}. Ninguém ganhou! Jogue outra vez!')
elif jogador == 'pedra' and computador == 'papel':
  print(f'Você PERDEU! Você jogou {jogador} e o computador {computador}!')
elif jogador == 'papel' and computador == 'pedra':
  print(f'Você GANHOU! Você jogou {jogador} e o computador {computador}!')
elif jogador == 'tesoura' and computador == 'pedra':
  print(f'Você PERDEU! Você jogou {jogador} e o computador {computador}!')
elif jogador == 'pedra' and computador == 'tesoura':
  print(f'Você GANHOU! Você jogou {jogador} e o computador {computador}!')
elif jogador == 'papel' and computador == 'tesoura':
  print(f'Você PERDEU! Você jogou {jogador} e o computador {computador}!')
elif jogador == 'tesoura' and computador == 'papel':
  print(f'Você GANHOU! Você jogou {jogador} e o computador {computador}!')

'''
opcao 2
from random import randint
lista = ['pedra', 'papel', 'tesoura']
computador = randint(0,2)
print(itens[computador])'''