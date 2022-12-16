#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('De qual número você deseja ver a tabuada? '))
print(f'=> Tabuada de {num} <=')
for numero in range(1, 11):
    print(f'{num} x {numero} = {num * numero}')
print('FIM!')