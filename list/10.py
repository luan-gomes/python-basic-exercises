"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um 
terceiro vetor de 20 elementos, cujos valores deverão ser compostos 
pelos elementos intercalados dos dois outros vetores.
"""

vetor1 = [ 0, 2, 4, 6, 8, 10, 12, 14, 16, 18 ]
vetor2 = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ]
vetor3 = []
i = 0

while i < 10:
	vetor3.append(vetor1[i])
	vetor3.append(vetor2[i])
	i+=1
	
print(vetor1)
print(vetor2)
print(vetor3)
