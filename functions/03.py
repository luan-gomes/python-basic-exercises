"""
Faça um programa, com uma função que necessite de três argumentos, e
que forneça a soma desses três argumentos.
"""

def soma(a, b, c):
	return a+b+c

lista = []

for i in range(1,4):
	valor = float(input("Digite um número: "))
	lista.append(valor)
	
resultado = soma(lista[0], lista[1], lista[2])
print(f"O resultado da soma é: {resultado:.2f}")
