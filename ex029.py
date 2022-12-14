#: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Velocidade (km/h): '))
total_ultrapassado = velocidade - 80
multa = total_ultrapassado * 7
if velocidade > 80:
    print(f'''Você está dirigindo {total_ultrapassado}km/h a mais que o permitido!Multa devida: R${multa:,.2f}Lembre-se que o limite de velocidade é de 80km/h!''')
else:
    print(f'Você está dirigindo dentro da velocidade permitida.Continue assim!')
