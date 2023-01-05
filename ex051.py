inicio = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

print("Os 10 primeiros termos dessa progressão são: ")
for x in range(0, 10):
    print(inicio, end=" ")
    inicio += razao
