# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
full_name = str(input('Digite seu nome completo: ')).lower().split()
first_name = full_name[0].capitalize()
last_name = full_name[len(full_name) -1].capitalize()
print(f'''Nome: {first_name}
Sobrenome: {last_name} ''')
