#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Informe a quantidade de Km percorridos: '))
dias = int(input('Informe a quantidade de dias em que o carro foi alugado: '))
preco = km * 0.15 + dias * 60
print(f'Para {km} percorridos e {dias} dias de aluguel, o valor total a pagar é R${preco:,.2f}')
