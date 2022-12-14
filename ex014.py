# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Informe a temperatura em Celsius: '))
fahrenheit = celsius * 1.8 + 32
print(f'A temperatura {celsius} em Celsius, corresponde a {fahrenheit} Fahrenheit.')