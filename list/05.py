"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
"""

par = []
impar = []

for i in range( 1, 21 ):
	numero = int(input("Digite um número: "))
	if numero%2 == 0:
		par.append(numero)
	else:
		impar.append(numero)
		
print(par)
print(impar)
