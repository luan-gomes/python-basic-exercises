#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = [ 123, 254, 2, 18, 69  ]
soma = 0
produto = 1

for numero in vetor:
	print(numero)
	soma+=numero
	produto*=numero

print(f"A soma dos valores do vetor: {soma}")
print(f"O produto da multiplicação dos valores: {produto}")

