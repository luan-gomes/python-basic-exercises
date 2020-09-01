"""
04)
Supondo que a população de um país A seja da ordem de 80000 habitantes 
com uma taxa anual de crescimento de 3% e que a população de B seja 
200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para
que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.

05
Altere o programa anterior permitindo ao usuário informar as populações 
e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""

continuar = "sim"

while continuar.lower() == "sim":
	while True:
		populacao_a = int(input("População do país A: "))
		populacao_b = int(input("População do país B: "))
		taxa_a = float(input("Taxa de crescimento do país A: "))
		taxa_b = float(input("Taxa de crescimento do país B: "))

		if (populacao_a > 0 and populacao_b > 0) and (0 < taxa_a <=1 and 0 < taxa_b <=1):
			break
		else:
			print("A população de um país não pode ser menor do que zero.")
			print("A taxa de crescimento deve ser entre 0 e 1.")
			
	ano = 1

	while populacao_a < populacao_b:
		populacao_a += populacao_a * taxa_a
		populacao_b += populacao_b * taxa_b
		ano+=1

	print(f"Ano {ano} - População A = {populacao_a:.0f} | População B = {populacao_b:.0f}")
	print(f"A População de A levou {ano} anos para superar/igualar a de B!")
	
	continuar = input("Deseja continuar?")
