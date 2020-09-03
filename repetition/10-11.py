"""
10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
11 - Altere o programa anterior para mostrar no final a soma dos números.
"""

n1 = int(input("Informe o início do intervalo: "))
n2 = int(input("Informe o fim do intervalo: "))
soma = 0

if n1 < n2:
	for i in range( n1, n2+1 ):
		soma+=i
		print(i)
else:
	for i in range( n1, n2-1, -1 ):
		soma+=i
		print(i)	
print(f"Soma: {soma}")
