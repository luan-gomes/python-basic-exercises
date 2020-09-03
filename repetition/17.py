"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120
"""

while True:
	number = int(input("Digite um número: "))
	if number > 0:
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
