"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e 
armazene num vetor a média de cada aluno, imprima o número de alunos 
com média maior ou igual a 7.0.
"""

medias = []
aprovados = 0

for i in range(1,11):
	soma_notas = 0
	for x in range(1,5):
		nota = float(input(f"Informe a nota {x} do aluno {i}: "))
		soma_notas+=nota
	media = soma_notas/4
	if media >= 7:
			aprovados+=1
	medias.append(media)

print(medias)
print(f"{aprovados} alunos tiveram média maior ou igual a 7.0")
