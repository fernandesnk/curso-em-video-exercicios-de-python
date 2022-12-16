#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
  print(f'IMC: {imc:,.1f} Classificação: ABAIXO DO PESO')
elif imc < 25:
  print(f'IMC: {imc:,.1f} Classificação: PESO IDEAL')
elif imc < 30:
  print(f'IMC: {imc:,.1f} Classificação:SOBREPESO')
elif imc < 40:
  print(f'IMC: {imc:,.1f} Classificação: OBESIDADE')
else:
  print(f'IMC: {imc:,.1f} Classificação: OBESIDADE MÓRBIDA')
