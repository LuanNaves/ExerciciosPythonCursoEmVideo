soma_idade = 0
homem_mais_velho = ""
idade_mais_velho = 0
mulher_menor_20 = 0
for pessoa in range(1, 5):
    print("-" * 5, f"{pessoa}ª PESSOA", "-" * 5)
    nome = str(input("Nome: ")).strip().title()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M/F): ")).strip().upper()
    soma_idade += idade
    if sexo == "F" and idade < 20:
        mulher_menor_20 += 1
    if sexo == "M" and idade > idade_mais_velho:
        homem_mais_velho = ""
        homem_mais_velho += nome
        idade_mais_velho += idade
media = soma_idade / 4
print(f"""A média das idades é {media}
{mulher_menor_20} mulheres tem menos de 20 anos
O homem mais velho é o {homem_mais_velho}""")
