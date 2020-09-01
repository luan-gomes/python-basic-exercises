#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

value = int(input("Informe um número inteiro: "))

if value < 0:
	print(f"{value} é um valor negativo!")
elif value > 0:
	print(f"{value} é um valor positivo!")
else:
	print(f"{value} é um valor nulo!")
