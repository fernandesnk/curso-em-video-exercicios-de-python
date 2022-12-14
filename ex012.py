#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Preço do produto: R$ '))
novo_preco = preco - (preco * 0.05)
print(f'Com 5% de desconto o preço do produto passará a ser de R$ {novo_preco:,.2f}')