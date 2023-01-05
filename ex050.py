soma = 0
for x in range(1, 7):
    num = int(input(f"Digite o {x}º número: "))
    if num % 2 == 0:
        soma += num
print(f"A soma dos números PARES digitados é {soma}")
