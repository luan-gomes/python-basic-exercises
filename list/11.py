#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor1 = [ 0, 3, 6, 9, 12, 15, 18, 21, 24, 27 ]
vetor2 = [ 1, 4, 7, 10, 13, 16, 19, 22, 25, 28 ]
vetor3 = [ 2, 5, 8, 11, 14, 17, 20, 23, 26, 29 ]
vetor4 = []
i = 0

while i < 10:
	vetor4.append(vetor1[i])
	vetor4.append(vetor2[i])
	vetor4.append(vetor3[i])
	i+=1
	
print(vetor1)
print(vetor2)
print(vetor3)
print(vetor4)
