"""
Faça um programa que, dado um conjunto de N números, determine o menor 
valor, o maior valor e a soma dos valores
"""

continuar = "sim"
conjunto = []
maior = -1
menor = -1
soma = 0

while continuar.lower() == "sim":
	novo_numero = int(input("Digite um número: "))
	if novo_numero > 0:
		conjunto.append(novo_numero)
		
		if maior == -1 and menor == -1:
			maior = novo_numero
			menor = novo_numero
		else:
			if novo_numero > maior:
				maior = novo_numero
			if novo_numero < menor:
				menor = novo_numero
				
		soma+=novo_numero
		continuar = input("Deseja adicionar outro número? ")
	else:
		print("Digite um número inteiro positivo!")

		
print(f"Menor número: {menor}\nMaior número: {maior}\nSoma: {soma}")

