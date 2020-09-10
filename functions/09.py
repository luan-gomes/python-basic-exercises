#Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(numero):
	convertido = str(numero)
	inverso = ""
	for x in range(len(convertido)-1,-1,-1):
		inverso+=convertido[x]
	return inverso
	
valor = int(input("Informe um número: "))
resposta = reverso(valor)
print(f"O inverso de {valor} é: {resposta}.")
