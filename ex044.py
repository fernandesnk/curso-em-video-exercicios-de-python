#Elabore um programa que calcule o valor a ser pago por um produto, 
#considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros
preco = float(input('Preço: R$ '))
print('''Formas de pagamento:
1-à vista dinheiro ou cheque 
2- à vista no cartão
3- em até 2x no cartão
4- 3x ou mais no cartão ''')
pagamento = int(input('Digite o nº da opção escolhida: '))
if pagamento == 1:
  novo_preco = preco * 0.9
  print(f'Para essa modalidade de pagamento, há desconto de 10%, portanto você pagará R${novo_preco:,.2f}.')
elif pagamento == 2:
  novo_preco = preco * 0.95
  print(f'Para essa modalidade de pagamento, há desconto de 5%, portanto você pagará R${novo_preco:,.2f}.')
elif pagamento == 3:
  print(f'Para essa modalide de pagamento não há aplicação de desconto, portanto você pagará R${preco:,.2f}.')
else:
  novo_preco = preco * 1.2
  parcelas = int(input('Em quantas parcelas deseja pagar? '))
  valor_parcela = novo_preco / parcelas
  print(f'''Para essa modalidade de pagamento há a aplicação de 20% de juros.
Você pagará {parcelas} parcelas de R${valor_parcela:,.2f} totalizando R${novo_preco:,.2f}.''')