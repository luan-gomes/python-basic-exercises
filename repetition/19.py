#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

continuar = "s"
conjunto = []
maior = -1
menor = -1
soma = 0

while continuar.lower() == "s":
	novo_numero = int(input("Digite um número: "))
	if 0 < novo_numero < 1000:
		conjunto.append(novo_numero)
		
		if maior == -1 and menor == -1:
			maior = novo_numero
			menor = novo_numero
		else:
			if novo_numero > maior:
				maior = novo_numero
			if novo_numero < menor:
				menor = novo_numero
				
		soma+=novo_numero
		continuar = input("Deseja adicionar outro número? ")
	else:
		print("Digite um número entre 0 e 1000!")

		
print(f"Menor número: {menor}\nMaior número: {maior}\nSoma: {soma}")


