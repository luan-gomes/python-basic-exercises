#Faça um Programa que leia três números e mostre o maior e o menor deles.

a = float(input("Informe o primeiro número: "))
b = float(input("Informe o segundo número: "))
c = float(input("Informe o terceiro número: "))

if a > b and a> c:
	if b < c:
		print(f"Maior: {a}\nMenor: {b}")
	else:
		print(f"Maior: {a}\nMenor: {c}")
	
elif b > a and b > c:
	if a < c:
		print(f"Maior: {b}\nMenor: {a}")
	else:
		print(f"Maior: {b}\nMenor: {c}")
else:
	if a < b:
		print(f"Maior: {c}\nMenor: {a}")
	else:
		print(f"Maior: {c}\nMenor: {b}")
