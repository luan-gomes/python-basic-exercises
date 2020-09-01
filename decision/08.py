"""
Faça um programa que pergunte o preço de três produtos e informe qual 
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
print("Informe o valor de três produtos e irei te dizer qual o mais barato para comprar!")

p1 = float(input("Valor do primeiro produto: "))
p2 = float(input("Valor do segundo produto: "))
p3 = float(input("Valor do terceiro produto: "))

if p1 < p2 and p1 < p3:
	print(f"Você deve comprar o primeiro produto por R${p1}")
elif p2 < p1 and p2 < p3:
	print(f"Você deve comprar o segundo produto por R${p2}")
else: 
	print(f"Você deve comprar o terceiro produto por R${p3}")
