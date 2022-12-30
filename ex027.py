nome = str(input("Digite o seu nome: ")).strip().title()
separado = nome.split()
print(f"Primeiro nome: {separado[0]}")
print(f"Último nome: {separado[len(separado) - 1]}")
