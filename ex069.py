maioridade = 0
total_homens = 0
mulheres_menos_de_20 = 0
while True:
    print("-" * 22)
    print("CADASTRE UMA PESSOA")
    print("-" * 22)
    while True:
        idade = int(input("Idade: "))
        if idade < 0:
            print("Valor Inválido.")
        else:
            break
    while True:
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if sexo not in "MF":
            print("Valor Inválido.")
        else:
            break
    if idade > 18:
        maioridade += 1
    if sexo == "M":
        total_homens += 1
    if sexo == "F" and idade < 20:
        mulheres_menos_de_20 += 1
    while True:
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if continuar not in "SN":
            print("Valor Inválido.")
        else:
            break
    if continuar == "N":
        print("-" * 22)
        print("CADASTROS FINALIZADOS")
        print("-" * 22)
        break
print(f"Total de pessoas com mais de 18 anos: {maioridade}")
print(f"Total de homens cadastrados: {total_homens}")
print(f"Total de mulheres com menos de 20 anos: {mulheres_menos_de_20}")
