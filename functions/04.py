"""
Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
 e ‘N’, se seu argumento for zero ou negativo.
"""

def sinal(numero):
	if numero > 0:
		return("Positivo")
	elif numero < 0:
		return("Negativo")
	else:
		return("Neutro")
		
valor = float(input("Digite um número: "))
resposta = sinal(valor)
print(f"{valor} é um número {resposta}")
