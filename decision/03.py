"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

sex = input("Qual o seu sexo biológico: F ou M?")

if sex.lower() == 'f':
	print("Você é do sexo feminino!")
elif sex.lower() == 'm':
	print("Você é do sexo masculino!")
else:
	print("Não definido!")
