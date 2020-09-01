"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar
M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
"Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

print("Considere os seguintes códigos para responder a questão a seguir:")
print("M - Matutino\nV - Vespertino\nN - Noturno")

answer = input("Em que turno você estuda? Utilize os códigos supracitados!")

if answer.lower() == 'm':
	print("Bom dia!")
elif answer.lower() == 'v':
	print("Boa tarde!")
elif answer.lower() == 'n':
	print("Boa noite!")
else:
	print("Valor Inválido!")
