#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_nascimento = int(input('Informe seu ano de nascimento: '))
idade = (date.today().year) - ano_nascimento
if idade < 18:
  anos_pendentes = 18 - idade
  print(f'Ainda não chegou a hora de se alistar, pois você tem apenas {idade} anos! Faltam {anos_pendentes} anos para o seu alistamento militar.')
elif idade == 18:
  print(f'Chegou a hora de se alistar! Você possui {idade} anos e já está apto a se apresentar ao exército.')
else:
  anos_excedidos = idade - 18
  print(f'O teu período de alistamento passou há {anos_excedidos} anos, pois sua idade é {idade} anos.')
