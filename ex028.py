#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
num = int(input('Chute um número inteiro de 1 a 5 : '))
num_sorteado = randint(1,5)
if 1 > num > 5:
    print('Atenção às instruções!Você deverá escolher um NÚMERO INTEIRO dentre estes: 1,2,3,4 ou 5. ')
elif num == num_sorteado:
    print(f'Parabéns! Você adivinhou o número sorteado! Você escolheu {num} e o computador sorteou {num_sorteado}!')
else:
    print(f'Que pena, você errou! Você escolheu o número {num}, e o computador sorteou {num_sorteado}.Tente outra vez!')