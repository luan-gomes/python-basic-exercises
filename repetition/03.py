"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
	nome = input("Digite o nome: ")
	if len(nome) > 3:
		break
	else:
		print("O nome deve ter mais de 3 caracteres.")
		
while True:
	idade = int(input("Digite a idade: "))
	if 0 <= idade <= 150:
		break
	else:
		print("A idade deve estar entre 0 e 150.") 

while True:
	salario = float(input("Digite o salário:"))
	if salario > 0:
		break
	else:
		print("O salário deve ser maior do que 0.00.")
		
		
while True:
	sexo = input("Digite o sexo (utilize f ou m):")
	if sexo.lower() == 'f' or sexo.lower() == 'm':
		break
	else:
		print("O sexo deve ser f ou m.")
		
while True:
	estado_civil = input("Digite o estado civil (utilize s, c, v ou d):")
	if estado_civil.lower() == 's' or estado_civil.lower() == 'c' or estado_civil.lower() == 'v' or sexo.lower() == 'd':
		break
	else:
		print("O estado civil deve ser s, c, v ou d.")
		
print(f"Nome: {nome}\nIdade: {idade}\nSalário: {salario}\nSexo: {sexo}\nEstado Civil: {estado_civil}")
