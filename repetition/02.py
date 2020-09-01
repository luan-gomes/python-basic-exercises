"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite 
a senha igual ao nome do usuário, mostrando uma mensagem de erro e 
voltando a pedir as informações.
"""

while True:
	username = input("Informe o nome do usuário: ")
	password = input("Informe a senha do usuário: ")

	if username != password:
		break
	else:
		print("ERRO! O nome a senha devem ser diferentes. Tente novamente.")

print("Acesso permitido!")
