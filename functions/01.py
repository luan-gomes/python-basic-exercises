"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""

def impressao(n):
	if n <= 0:
		print("Digite um número inteiro positivo.")
	else: 
		for x in range(1,n+1):
			repeticao = (str(x)+" ")*x
			print(repeticao)
		
numero = int(input("Digite um número: "))
impressao(numero)
