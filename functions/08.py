#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def quantDigitos(numero):
	convertido = str(numero)
	return len(convertido)
	
valor = int(input("Informe um número: "))
resposta = quantDigitos(valor)
print(f"O número {valor} tem {resposta} dígitos.")
