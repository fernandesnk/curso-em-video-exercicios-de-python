#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input('Informe o primeiro termo da P.A. : ')) #a1 -> primeiro termo
r = int(input('Informe a razão da P.A. : ')) # r -> razão
for x in range(1, 11):
    print(a1 + (x - 1) * r,  end= ' -> ' )


