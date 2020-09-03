"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
"""

n1 = 1
n2 = 1
current = 0
i = 1
sequencia = ""

while True:
	if current > 500:
		break
	else:
		if i == 1:
			sequencia+=str(n1)+", "
		elif i == 2:
			sequencia+=str(n2)+", "
		else:
			current = n1 + n2
			sequencia+=str(current)+", "
			n1 = n2
			n2 = current
	i+=1
sequencia+="..."
print(sequencia)
