"""
Faça um programa de implemente um jogo de Craps. 
O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na 
primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você
tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""
import random
random.seed()

jogada = 1
primeira_jogada = 0

while True:
	input()
	valor = random.randrange(2,12)
	
	if jogada == 1:
		
		if valor == 7 or valor ==11:
			print(f"Você tirou {valor} e ganhou! Parabéns! :D")
			break
		elif valor == 2 or valor == 3 or valor == 12:
			print(f"Você tirou {valor} e perdeu! :(")
			break
		else:
			primeira_jogada = valor
			print(f"Você tirou {valor}. Segue o jogo!")
		jogada += 1	
	else:
		
		if valor == primeira_jogada:
			print(f"Você tirou {valor} e é igual a {primeira_jogada}! Você ganhou :D")
			break
		elif valor == 7:
			print(f"Você tirou {valor} e perdeu! :(")
			break
		else: 
			print(f"Você tirou {valor} e precisa deum {primeira_jogada}. Jogue outra vez!")
		jogada += 1	
