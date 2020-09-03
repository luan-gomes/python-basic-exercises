"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular
o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""

continuar = "sim"

while continuar == "sim":
	while True:
		number = int(input("Digite um número: "))
		if 0 < number < 16:
			break
		else:
			print("O número precisa ser maior do que zero!")

	indice = number

	while indice > 0:
		if indice == number:
			fatorial = number
			indice-=1
		else:
			fatorial*=indice
			indice-=1

	print(f"O fatorial de {number} é: {fatorial}")
	continuar = input("Deseja calcular outro fatorial?")
