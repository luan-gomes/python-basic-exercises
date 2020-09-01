"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do 
outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""
print("Impressão vertical:\n")
for i in range(1,21):
	print(f"{i}")


side_by_side = ""
print("\nImpressão horizontal:\n")
for i in range(1,21):
	side_by_side += str(i)+" "
print(side_by_side)
