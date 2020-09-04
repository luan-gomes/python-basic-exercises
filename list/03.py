#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = [8, 8.5, 7, 9]
media = 0

for nota in notas:
	media+=nota

media/=4

print(f"A média das notas é: {media}")
