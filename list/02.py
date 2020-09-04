#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = [ 1, 2.5, 5, 10.8, 9, 55, 6.8, 10, 9.78, 0.85]
tamanho = len(vetor)-1

for i in range(tamanho, -1, -1):
	print(vetor[i])
