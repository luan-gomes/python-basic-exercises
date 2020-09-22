class Bola:
	
	def __init__(self, cor, circunferencia, material):
		self.cor = cor
		self.circunferencia = circunferencia
		self.material = material
		
	def trocarCor(self, novaCor):
		self.cor = novaCor
		
	def mostrarCor(self):
		print("A cor da bola é:",self.cor)
	
	
		
		
bola = Bola("azul",10,"plástico")
bola.trocarCor("Vermelho")
bola.mostrarCor()
