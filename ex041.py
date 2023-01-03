from datetime import date
data = int(input("Em que ano você nasceu? "))
idade = date.today().year - data
if 0 < idade <= 9:
    print("Sua categoria: MIRIM")
elif 9 < idade <= 14:
    print("Sua categoria: INFANTIL")
elif 14 < idade <= 19:
    print("Sua categoria: JÚNIOR")
elif 19 < idade <= 20:
    print("Sua categoria: SÊNIOR")
elif idade > 20:
    print("Sua categoria: MASTER")
else:
    print("Você não nasceu ainda meu querido.")
