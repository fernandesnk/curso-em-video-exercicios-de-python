#Escreva um programa em Python que leia um número inteiro qualquer e peça 
#para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número: '))
base_conversao = int(input('''Escolha a base de conversão:
Digite 1 para binário:
Digite 2 para octal:
Digite 3 para hexadecimal:  
'''))
if 1 > num > 3:
  print(f'Atenção às instruções! Você deverá digitar os números 1, 2 ou 3 para escolher a base de conversão!')
elif base_conversao == 1:
  binario = bin(num)
  print(binario[2:])
elif base_conversao == 2:
  octal = oct(num)
  print(octal[2:])
else:
  hexa = hex(num)
  print(hexa[2:])