"""
Faça um programa que peça 10 números inteiros, calcule e mostre a 
quantidade de números pares e a quantidade de números impares.
"""

numeros = []
pares = 0
impares = 0

for i in range(1,11):
	numeros.append(int(input("Digite um número inteiro: ")))
	
for i in range(0, len(numeros)):
	if(numeros[i]%2 == 0):
		pares+=1
	else:
		impares+=1
		
print(f"Números pares: {pares}\nNumeros Ímpares: {impares}")
