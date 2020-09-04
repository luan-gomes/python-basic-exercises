"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas 
consoantes foram lidas. Imprima as consoantes.
"""

caracteres = [ "f", "k", "i", "b", "i", "f", "j", "e", "a", "z" ]
quant_consoantes = 0
lista_consoantes = caracteres.copy()

for char in caracteres:
	if char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
		quant_consoantes+=1
	else: 
		lista_consoantes.remove(char)

print(f"Foram lidas {quant_consoantes}. Foram elas: ")
print(lista_consoantes)
