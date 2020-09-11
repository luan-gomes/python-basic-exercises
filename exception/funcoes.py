
def menu(saida, *opcao):
	i = 1

	for op in opcao:
		print(f"{i}: {op}")
		i += 1
	print(f"0: {saida}")
	
	return int(input(f"Escolha uma opção [0-{len(opcao)}]"))
