frase = str(input("Digite uma frase: ")).strip().lower().replace(" ", "")
inversa = ""
for letra in range(len(frase) - 1, -1, -1):
    inversa += frase[letra]
if frase == inversa:
    print("Essa frase é um palindromo.")
else:
    print("Essa frase não é um palindromo.")
