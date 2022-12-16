#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o teu salário? R$ '))
anos = int(input('Em quantos anos você irá pagar?'))
prestacao = valor_casa / (anos * 12)
condicao_emprestimo = salario * 0.3
if prestacao <= condicao_emprestimo:
  print(f'Empréstimo APROVADO!Você quitará o valor de R${valor_casa}, em parcelas mensais de R${prestacao:,.2f} por {anos} anos.')
else:
  diferenca = prestacao - condicao_emprestimo
  print(f'Empréstimo NEGADO!As prestações excederam em R${diferenca:,.2f} o valor limite estabelecido pelo banco.')