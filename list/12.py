"""
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos 
possuem altura inferior à média de altura desses alunos
"""

lista = [{"idade":13, "altura":1.6},{"idade":18, "altura":1.90},{"idade": 14, "altura": 1.50}]

adolescentes = []
totalAltura = 0

for aluno in lista:
	if aluno["idade"] > 13:
		adolescentes.append(aluno)
	totalAltura += aluno["altura"]

mediaAltura = totalAltura/len(lista)
abaixoMedia = 0

for aluno in adolescentes:
	if aluno["altura"] < mediaAltura:
		abaixoMedia += 1
		
print(f"{abaixoMedia} aluno(s) maior(es) de 13 anos tem altura menor do que {mediaAltura:.2f}")
