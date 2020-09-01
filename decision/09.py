#Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = float(input("Informe o primeiro número: "))
b = float(input("Informe o segundo número: "))
c = float(input("Informe o terceiro número: "))

if a > b and a > c:
	if b > c:
		print(f"{a}\n{b}\n{c} ")
	else:
		print(f"{a}\n{c}\n{b}")
elif b > a and b > c:
	if a > c:
		print(f"{b}\n{a}\n{c} ")
	else:
		print(f"{b}\n{c}\n{a}")
else:
	if a > b:
		print(f"{c}\n{a}\n{b} ")
	else:
		print(f"{c}\n{b}\n{a}")
