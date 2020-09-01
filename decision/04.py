#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letter = input("Informe uma letra!")

if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
	print(f"{letter} é uma vogal!")
else:
	print(f"{letter} é uma consoante!") 
