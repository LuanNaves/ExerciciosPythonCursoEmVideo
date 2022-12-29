frase = str(input("Digite uma frase: ")).upper().strip()
print(f"Na sua frase, a letra A aparece {frase.count('A')} vezes.")
print(f"A primeira letra A está na posição {frase.find('A') + 1}.")
print(f"A última letra A está na posição {frase.rfind('A') + 1}.")
