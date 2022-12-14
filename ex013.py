#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Informe seu salário atual: '))
novo_salario = salario + (salario * 0.15)
print(f'Após aumento de 15%, teu salário passou de R${salario:,.2f} para R${novo_salario:,.2f}!')
