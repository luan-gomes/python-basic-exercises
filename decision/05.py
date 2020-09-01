"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
	A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
	A mensagem "Reprovado", se a média for menor do que sete;
	A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

n1 = float(input("Informe a primeira nota do aluno: "))
n2 = float(input("Informe a segunda nota do aluno: "))
media = (n1+n2)/2

if media == 10:
	print("Aprovado com distinção!")
elif media >= 7:
	print(f"Aprovado com média {media}")
else:
	print(f"Reprovado com média {media}")
