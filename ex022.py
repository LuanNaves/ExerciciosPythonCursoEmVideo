nome = str(input("Digite seu nome completo: ")).strip()
partes = nome.split()
espacos = int(nome.count(' '))
print(f"Maiúsculas: {nome.upper()}")
print(f"Minúsculas: {nome.lower()}")
print(f"Número de letras: {len(nome) - espacos}")
print(f"Número de letras no primeiro nome: {len(partes[0])}")
