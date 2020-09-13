#Simulação de uma sistema de cadastro de lista de convidados

import funcoes 

lista_convidados = []

try:
	
	arquivo = open("convidados.txt","r")
	lista_convidados = arquivo.readlines()
	for i in range(len(lista_convidados)):
		lista_convidados[i] = lista_convidados[i].strip()
	
except FileNotFoundError:
	
	print("Arquivo não encontrado.")
	
except PermissionError:
	
	print("Você não tem permissão para acessar este arquivo.")

except IOError:
	
	print("Erro de E/S.")

else:
	
	arquivo.close()

while True:
	
	try: 
		opcao = funcoes.menu("Sair", "Adicionar convidado", "Remover convidados", "Exibir lista de convidados")
		
		if opcao == 0:
			
			try: 
				
				arquivo = open("convidados.txt","w")
				arquivo.writelines(lista_convidados)
				print("Arquivo gravado com sucesso!")
				
			except PermissionError:
				
				print("Você não tem permissão para acessar este arquivo.")

			except IOError:
				
				print("Erro de E/S.")
				
			else:
				
				arquivo.close()
				
			break
			
		elif opcao == 1:
			
			nome = input("Digite o nome do convidado que deseja cadastrar: ")
			lista_convidados.append(nome+"\n")
			print("Convidado cadastrado com sucesso!")
			
		elif opcao == 2:
			
			nome = input("Digite o nome do convidado que deseja excluir: ")
			encontrado = False
			for convidado in lista_convidados:
				if nome in convidado:
					lista_convidados.remove(convidado)
					encontrado = True
					print("Convidado removido da lista.")
					break
					
			if encontrado == False:
				print("Este nome não está na lista de convidados. Por isso, não foi possível removê-lo.")
				
		elif opcao == 3:
			
			i = 1
			print("="*5 + "LISTA DE CONVIDADOS" + "="*5)
			for convidado in lista_convidados:
				print(f"{i}) {convidado}")
				i += 1
				
	except ValueError:
		("Você digitou uma opção inválida. Tente novamente.")
	
