#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Informe o início do intervalo: "))
n2 = int(input("Informe o fim do intervalo: "))

if n1 < n2:
	for i in range( n1, n2+1 ):
		print(i)
else:
	for i in range( n1, n2-1, -1 ):
		print(i)	
