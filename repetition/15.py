"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo
"""

n = int(input("Digite um número: "))

n1 = 1
n2 = 1
n_current = 0
sequencia = ""

for i in range( 1, n+1 ):
	if i == 1:
		sequencia += str(n1)+", "
	elif i == 2:
		sequencia += str(n2)+", "
	else:
		current = n1+n2
		sequencia += str(current)+", "
		n1 = n2
		n2 = current

sequencia +="..."
print(sequencia)
