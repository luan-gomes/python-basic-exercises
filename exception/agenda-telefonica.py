lista = []

while True:
	
	print("1) Adicionar contato")
	print("2) Remover contato")
	print("3) Exibir agenda")
	print("0) Sair")
	
	try:
		opcao = int(input("Digite uma opção [0-3]: "))
		
		if opcao == 0:
			break
			
		elif opcao == 1:
			nome = input("Informe o nome do contato: ")
			telefone = input("Informe o número do contato: ")
			nome = nome.strip()
			telefone = telefone.strip()
			print(f"{nome} {telefone}")
			
			if nome == "" or telefone == "":
				print("Nome e telefone são campos obrigatórios!")
			else:				
				contato_novo = {"nome":nome, "telefone":telefone}
				lista.append(contato_novo)
				print("Contato adicionado!")
		elif opcao == 2:
			nome = input("Informe o nome do contato que deseja remover: ")
			contato_encontrado = False
			
			for contato in lista:
				if contato["nome"] == nome:
					contato_encontrado = True
					lista.remove(contato)
					print("Contato removido.")
					break
			
			if contato_encontrado == False:
				print("O contato não foi encontrado.")
			
		elif opcao == 3:
			
			print("\n----- AGENDA TELEFÔNICA -----\n")
			for contato in lista:
				print(f"Nome: {contato['nome']} | Telefone: {contato['telefone']}")
			
		else: 
			print("Opção inválida!")
	except ValueError:
		print("Você digitou uma opção inválida!")
