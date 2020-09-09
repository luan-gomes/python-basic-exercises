"""
Faça um programa que peça um número inteiro e determine se ele é ou não 
um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

primo = True
numero = int(input("Informe um número: "))

for x in range(1,10):
	if numero != x and x != 1:
		resto = numero%x
		if resto == 0:
			primo = False
			break
	
if primo is True:
	print("O número é primo!")
else:
	print("O número não é primo!")
