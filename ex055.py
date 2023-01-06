lista = []
for pessoa in range(1, 6):
    peso = float(input(f"Peso da {pessoa}ª pessoa: "))
    lista.append(peso)
lista.sort()
print(f"O maior peso foi de {lista[4]:.2f}Kg e o menor foi {lista[0]:.2f}Kg")
