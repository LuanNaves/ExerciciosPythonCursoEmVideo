continuar = "S"
soma = 0
count = 0
lista = []
while continuar == "S":
    num = int(input("Digite um número inteiro: "))
    soma += num
    lista.append(num)
    continuar = str(input("Quer continuar? (S / N) ")).strip().upper()[0]
    count += 1
media = soma / count
lista.sort()
print(f"O maior valor digitado foi {lista[count - 1]}, e o menor foi {lista[0]}")
print(f"A média de todos os valores é {media:.2f}")
