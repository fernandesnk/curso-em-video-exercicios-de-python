#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Informe seu salário: R$ '))
if salario <= 1250:
    novo_salario = salario * 1.15
    print(f'Com um aumento de 15% teu novo salário será de R$ {novo_salario:,.2f}')
else:
    novo_salario = salario * 1.10
    print(f'Com um aumento de 10% teu novo salário será de R$ {novo_salario:,.2f}')
