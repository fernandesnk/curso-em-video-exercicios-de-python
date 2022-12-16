#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
  print(f'As retas {r1}, {r2} e {r3} formam um TRIÂNGULO!')
  if r1 == r2 == r3:
    print(f'E o triângulo formado é EQUILÁTERO!')
  elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
    print(f'E o triângulo formado é ISÓSCELES!')
  else:
    print(f'E o triângulo formado é ESCALENO!')
else:
  print(f'As retas {r1}, {r2} e {r3} NÃO FORMAM um triângulo!')
