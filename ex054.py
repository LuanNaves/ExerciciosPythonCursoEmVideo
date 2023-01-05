from datetime import date
de_maior = 0
de_menor = 0
for pessoa in range(1, 8):
    ano = int(input(f"Ano de nascimento da {pessoa}ª pessoa: "))
    idade = date.today().year - ano
    if idade >= 18:
        de_maior += 1
    else:
        de_menor += 1
if de_maior == 7:
    print("Dessas 7 pessoas, todas atingiram a maioridade.")
elif de_menor == 7:
    print("Dessas 7 pessoas. nenhuma atingiu a maioridade ainda.")
else:
    print(f"Dessas 7 pessoas, {de_menor} ainda não atingiram a maioridade, ", end="")
    print(f"e {de_maior} já atingiram a maioridade.")
