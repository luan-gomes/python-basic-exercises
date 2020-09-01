#Faça um programa que leia 5 números e informe o maior número.

maior = -1

for i in range(5):
	numero = int(input("Informe um numero: "))
	if numero > maior:
		maior = numero

print(f"O maior número é: {maior}")
	
