nota1 = float(input("Valor da primeira nota: "))
nota2 = float(input("Valor da segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Sua média foi de {media:.1f}")
if media >= 7:
    print("PARABÉNS!")
    print("Você foi APROVADO!")
elif media < 5:
    print("Você foi REPROVADO.")
    print("Estude mais!")
else:
    print("Você está de RECUPERAÇÃO.")
    print("Estude mais!")
