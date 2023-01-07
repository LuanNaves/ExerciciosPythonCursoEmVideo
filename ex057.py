sexo = str(input("Informe seu sexo: (M / F) ")).strip().upper()[0]
while sexo not in "MF":
    print("Valor inválido.")
    sexo = str(input("Informe seu sexo: (M / F) ")).strip().upper()[0]
print(F"Sexo {sexo} registrado com sucesso.")