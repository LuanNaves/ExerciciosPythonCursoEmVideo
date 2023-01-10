inicio = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
count = 0
print("Os 10 primeiros termos dessa PA são: ")
while count < 10:
    print(inicio, end=" -> ")
    inicio += razao
    count += 1
print("PAUSA")
mais_termos = int(input("Deseja ver mais quantos termos? "))
while mais_termos != 0:
    count = 0
    while count < mais_termos:
        print(inicio, end=" -> ")
        inicio += razao
        count += 1
    print("PAUSA")
    mais_termos = int(input("Deseja ver mais quantos termos? "))
print("FIM")
