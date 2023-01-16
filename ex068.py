from random import randint
vitoria = 0
print("\033[36m-=" * 6, end="-\n")
print("\033[1;34mPAR\033[m ou \033[1;31mIMPAR\033[m")
print("\033[36m-=" * 6, end="-\n")
while True:
    computador = randint(0, 10)
    escolha = str(input("\033[mEscolha: PAR OU IMPAR? [P / I] ")).upper().strip()[0]
    if escolha not in "IP":
        print("Escolha inválida")
    else:
        jogador = int(input("Escolhe um número: "))
        if jogador < 0:
            print(f"Como você tem {jogador} dedos???? Impossível!")
        elif jogador > 10:
            print(f"Você tem mais de 10 dedos?? Improvavel.")
            print(f"Mas se tiver, mostre 10 ou menos dedos para jogar. Precisamos ser justos.")
        else:
            soma = computador + jogador
            if soma % 2 == 0:
                resultado = "PAR"
            else:
                resultado = "IMPAR"
            print("\033[36m-\033[m" * 20)
            print(f"O computador jogou {computador}")
            print(f"{jogador} mais {computador} é igual a {soma} que é {resultado}.")
            if escolha == "P" and resultado == "PAR":
                print("Você GANHOU!")
                print("Vamos jogar novamente.")
                vitoria += 1
            elif escolha == "I" and resultado == "IMPAR":
                print("Você GANHOU!")
                print("Vamos jogar novamente.")
                vitoria += 1
            else:
                print("Você PERDEU!")
                print("\033[36m-" * 20)
                break
    print("\033[36m-" * 20)
print("\033[1;34mGAME \033[1;31mOVER")
print(f"\033[mVocê teve uma sequencia de {vitoria} vitorias.")
