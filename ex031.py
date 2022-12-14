#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Informe a distância a ser percorrida: '))
if distancia <= 200:
    preco_passagem = distancia * 0.50
    print(f'Para uma distancia de {distancia}km, a passagem custa R${preco_passagem:,.2f}')
else:
    preco_passagem = distancia * 0.45
    print(f'Para uma distância de {distancia}km, a passagem custa R${preco_passagem:,.2f}')
