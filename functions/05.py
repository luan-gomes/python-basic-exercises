"""
Faça um programa com uma função chamada somaImposto. A função possui 
dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre 
vendas expressa em porcentagem e custo, que é o custo de um item antes do
imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

def taxaImposto(taxaImposto, custo):
	valorImposto = custo*taxaImposto
	valorFinal = custo + valorImposto
	return valorFinal

valor = float(input("Informe o custo do produto: "))
taxa = float(input("Informe a taxa do imposto: "))
resultado = taxaImposto(taxa,valor)
print(f"O valor de venda é: {resultado}")
