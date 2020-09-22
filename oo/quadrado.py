
class Quadrado:
	
	def __init__(self, tamanhoLado):
		self.tamanhoLado = tamanhoLado
		print("Quadrado criado!")
	
	def mudarValorLado(self, novoValor):
		self.tamanhoLado = novoValor
		
	def valorLado(self):
		return self.tamanhoLado
		
	def areaQuadrado(self):
		area = self.tamanhoLado*self.tamanhoLado
		print(area)
		
quadrado = Quadrado(10)
quadrado.mudarValorLado(15)
valor = quadrado.valorLado()
print(valor)
quadrado.areaQuadrado()
