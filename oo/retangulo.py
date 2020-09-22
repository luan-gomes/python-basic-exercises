
class Retangulo:
	
	def __init__(self, comprimento, altura):
		self.comprimento = comprimento
		self.altura = altura
		
	def getAltura(self):
		return self.altura
		
	def getComprimento(self):
		return self.comprimento
		
	def setAltura(self, novaAltura):
		self.altura = novaAltura
		
	def setComprimento(self, novoComprimento):
		self.comprimento = novoComprimento
		
	def area(self):
		area = self.altura*self.comprimento
		return area
		
	def perimetro(self):
		perimentro = self.altura+self.comprimento
		return perimetro
