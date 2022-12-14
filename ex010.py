# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
real = float(input('Quantos reais você possui? R$ '))
dolar = real/ 5.22
print(f'Com R${real:,.2f} você poderá comprar US${dolar:,.2f}!')