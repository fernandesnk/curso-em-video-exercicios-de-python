# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l = float(input('Informe a largura da parede: '))
h = float(input('Informe a altura da parede: '))
area = l * h
tinta = area/2
print(f'Para uma área de {area:,.3f}m², serão necessários {tinta:,.2f}L de tinta!')
