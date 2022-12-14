# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# opcao 1
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o primeiro número: '))
n3 = int(input('Digite o primeiro número: '))
if n3 < n1 > n2 and n3 > n2:
    print(f'{n1} é o MAIOR número, e {n2} é o MENOR número.')
elif n3 < n1 > n2 and n3 > n2 and n2 > n3:
      print(f'{n1} é o MAIOR número, e {n3} é o MENOR número.')
elif n3 < n2 > n1 and n3 > n1:
    print(f'{n2} é o MAIOR número, e {n1} é o MENOR número.')
elif n3 < n2 > n1 and n1 > n3:
    print(f'{n2} é o MAIOR número, e {n3} é o MENOR número.')
elif n2 < n3 > n1 and n2 > n1:
    print(f'{n3} é o MAIOR número, e {n1} é o MENOR número.')
else:
    print(f'{n3} é o MAIOR número, e {n2} é o MENOR número.')

'''opcao 2:
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o primeiro número: '))
n3 = int(input('Digite o primeiro número: '))
lista = [n1, n2, n3]
print(max(lista), min(lista))'''