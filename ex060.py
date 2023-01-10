num = int(input("Digite um número para ver o seu fatorial: "))
fatorial = num
print(f"{num}! é igual a", end=" ")
while num > 1:
    fatorial = fatorial * (num - 1)
    num -= 1
print(fatorial)
