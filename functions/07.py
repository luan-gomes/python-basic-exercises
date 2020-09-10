"""
1) Faça um programa que use a função valorPagamento para determinar o 
valor a ser pago por uma prestação de uma conta. 

2) O programa deverá solicitar ao usuário o valor da prestação e o número
de dias em atraso e passar estes valores para a função valorPagamento, 
que calculará o valor a ser pago e devolverá este valor ao programa que 
a chamou. O programa deverá então exibir o valor a ser pago na tela. 

3) Após a execução, o programa deverá voltar a pedir outro valor de 
prestação e assim continuar até que seja informado um valor igual a zero
para a prestação. Neste momento o programa deverá ser encerrado, exibindo 
o relatório do dia, que conterá a quantidade e o valor total de prestações
pagas no dia. 
 
4)O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos
sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3%
de multa, mais 0,1% de juros por dia de atraso.
"""

def valorPagamento(valorPrestacao, diasAtraso):
	if diasAtraso == 0:
		return valorPrestacao
	else: 
		multa = 0.03 * valorPrestacao
		jurosAoDia = (0.001*diasAtraso) * valorPrestacao
		valorAPagar = valorPrestacao + multa + jurosAoDia
		return valorAPagar

montanteDoDia = 0
quantidade = 0
	
while True:
	prestacao = float(input("Informe o valor da prestação: "))
	dias = int(input("Informe quantos dias de atraso: "))
	
	if prestacao == 0:
		print("-"*5+" RELATÓRIO DO DIA "+"-"*5)
		print(f"Quantidade de contas pagas: {quantidade}")
		print(f"Montante total: {montanteDoDia}")
		break
	else: 
		valor = valorPagamento(prestacao, dias)
		print(f"Valor a ser pago: {valor}")
		quantidade += 1
		montanteDoDia += valor
