n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
lista = [n1, n2, n3]
lista.sort()
print(f"Maior número: {lista[2]}")
print(f"Menor número: {lista[0]}")
