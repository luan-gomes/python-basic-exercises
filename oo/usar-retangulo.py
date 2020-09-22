import retangulo

def quantidadeDePisos(piso, area):
	piso = piso*0.0001
	total = area/piso
	margem = total*0.1
	total +=margem
	return int(total)


altura = float(input("Valor da altura do terreno: "))
comprimento = float(input("Valor do comprumento do terreno: "))

piso = float(input("Medida do piso em cm²: "))

terreno = retangulo.Retangulo(comprimento, altura)
area = terreno.area()

qtd = quantidadeDePisos(piso, area)

print(f"Serão necessários {qtd} pisos!")


