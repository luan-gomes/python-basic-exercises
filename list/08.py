"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem 
inversa a ordem lida.
"""

informacoes = []
i = 1

while i <= 5:
	altura = float(input("Informe sua altura em metros: "))
	idade = int(input("Informe a sua idade: "))
	pessoa = [ idade, altura ]
	informacoes.append(pessoa)
	i+=1

informacoes.reverse()

indice = 1
for pessoa in informacoes:
	print(f"Pessoa {indice}: Idade = {pessoa[0]} | Altura = {pessoa[1]}")
	indice+=1
