num = int(input("Digite um número de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
if 0 <= num < 10000:
    print(f"Analise do número {num}")
    print(f"Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}")
else:
    print("Número inválido.")
