#Faça um Programa que leia três números e mostre o maior deles.

a = float(input("Informe o primeiro número: "))
b = float(input("Informe o segundo número: "))
c = float(input("Informe o terceiro número: "))

if a > b and a> c:
	print(f"{a} é maior do que {b} e {c}!")
elif b > a and b > c:
	print(f"{b} é maior do que {a} e {c}!")
else:
	print(f"{c} é maior do que {b} e {a}!")
