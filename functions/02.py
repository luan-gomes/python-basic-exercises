"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""

def impressao(n):
	if n <= 0:
		print("Digite um número inteiro positivo.")
	else:
		for x in range(1,n+1):
			numero = 1
			linha = ""
			while numero <= x:
				linha += str(numero)+" "
				numero += 1
			print(linha)

valor = int(input("Digite um número inteiro positivo: "))
impressao(valor)
