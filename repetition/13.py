"""
Faça um programa que peça dois números, base e expoente, calcule e mostre
o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
"""

base = int(input("Digite um número: "))
expoente = int(input("Digite outro número: "))
i = 1
potencia = 1

while i <= expoente:
	potencia*=base
	i+=1
	
print(f"{base} ^ {expoente} = {potencia}") 
	
