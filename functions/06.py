"""
Faça um programa que converta da notação de 24 horas para a notação de 
12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: 
uma para fazer a conversão e uma para a saída.
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para 
P.M. Assim, a função para efetuar as conversões terá um parâmetro 
formal para registrar se é A.M. ou P.M. Inclua um loop que permita que 
o usuário repita esse cálculo para novos valores de entrada todas as 
vezes que desejar.
"""

def converter(horas, minutos):
	
	if horas >= 0 and horas <=24 and minutos >=0 and minutos <=60:
		
		if minutos == 60:
			horas+=1
			minutos = 0
		
		fator = horas /12
		
		if fator < 1:
			imprimir(horas, minutos,"A")
		elif fator == 1:
			imprimir(horas, minutos,"P")
		elif fator > 1 and fator < 2:
			horasConvertidas = horas-12
			imprimir(horasConvertidas, minutos,"P")
		elif fator == 2:
			imprimir(0, minutos,"A")
		
	else:
		print("Entrada inválida!")
		
def imprimir(horas, minutos, turno):
	
	if turno in "A":
		print(f"Horário convertido : {horas}:{minutos} A.M.")
	elif turno in "P":
		print(f"Horário convertido : {horas}:{minutos} P.M.")
	else:
		print("Valor inválido!")
		
continuar = "s"

while continuar == "s":
	h = int(input("Digite as horas: "))
	m = int(input("Digite os minutos: "))
	
	converter(h,m)
	
	continuar = input("Deseja continuar? [s ou n]")
