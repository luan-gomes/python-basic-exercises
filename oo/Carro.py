
class Carro:
	
	def __init__(self, marca, modelo, cor):
		self.marca = marca
		self.modelo = modelo
		self.cor = cor
		
	def ligar(self):
		print("Ligando o carro!")

	def desligar(self):
		print("Desligando o carro!")
		
	def exibirInformacoes(self):
		print(self.marca, self.modelo, self.cor)
	
carro = Carro("Chevrolet", "Tracker", "Branco")
carro.ligar()
carro.desligar()
carro.exibirInformacoes()
