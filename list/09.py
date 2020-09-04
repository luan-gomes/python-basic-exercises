"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule 
e mostre a soma dos quadrados dos elementos do vetor.
"""

vetor = [ 8, 11, 2, 9, 30, 7, 15, 56, 42, 13]
soma = 0

for numero in vetor:
	quadrado = numero**2
	soma+=quadrado
	print(f"{numero}^2 = {quadrado}")
	
print(f"A soma dos quadrados é: {soma}")
