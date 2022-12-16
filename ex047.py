#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
lista_pares = []
for numero in range (1, 51):
    if numero % 2 == 0:
        lista_pares.append(numero)
print(lista_pares)

'''outra opcao
for numero in range (1, 51):
    if numero % 2 == 0:
        print(numero, end=' ')'''
        

