#Simulação de uma agenda telefônica

import funcoes as f
import json

lista = []

#Ao iniciar o programa, verificar se já existe uma agenda.

try:
	
	arquivo = open("agenda.json","r")
	lista = json.load(arquivo)
	
except FileNotFoundError:
	print("Arquivo não encontrado.")

except PermissionError:
	print("Você não tem permissão para acessar este arquivo.")

except IOError:
	print("Erro de E/S.")
	
except json.decoder.JSONDecodeError:
	print("O arquivo não está em formato JSON.")
	
else:
	arquivo.close()


while True:
	
	try:
		opcao = f.menu("Sair","Adicionar contato","Remover contato","Exibir agenda")
		print(opcao)
		if opcao == 0:
			try:
				arquivo = open("agenda.json","w")
				json.dump(lista,arquivo)
			except PermissionError:
				print("Você não tem permissão para acessar este arquivo.")
			except IOError:
				print("Erro de E/S.")
			else:
				arquivo.close()				
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
