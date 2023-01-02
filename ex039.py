from datetime import date
ano = int(input("Em qual ano você nasceu? "))
idade = date.today().year - ano
if idade < 18:
    print("Ainda não está na hora!")
    print(f"Faltam {18 - idade} anos para poder se alistar.")
elif idade > 18:
    print("Se você não tiver se alistado ainda, você está atrasado!")
    print(f"Já se passaram {idade - 18} anos do prazo do seu alistamento.")
else:
    print("Está na hora, chegou o momento de se alistar!")
