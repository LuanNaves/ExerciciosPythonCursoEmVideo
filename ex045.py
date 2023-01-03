import random
import emoji
from time import sleep

lista = ["Pedra", "Papel", "Tesoura"]  # Possibilidades que o computador pode escolher

print("\033[35m=" * 11)
print("\033[1;31mJO \033[1;34mKEN \033[1;32mPÔ!!")
print("\033[35m=" * 11)

jogador = str(input("\033[mPedra, Papel ou Tesoura? ")).strip().title()  # Pega a escolha do jogador
computador = lista[random.randint(0, 2)]  # Gera um número aleatorio para definir a escolha do computador

print("\033[1;31mJO")
sleep(0.4)
print("\033[1;34mKEN")
sleep(0.4)
print("\033[1;32mPÔ!!\033[m")

if jogador == "Pedra" or jogador == "Papel" or jogador == "Tesoura":  # Verifica se o jogador digitou um valor válido
    print(emoji.emojize(f":computer: Computador: {computador}", language="alias"))  # Mostra a jogada do computador
    print(emoji.emojize(f":smile: Você: {jogador}", language="alias"))  # Mostra a jogada do jogador
    if computador == "Pedra" and jogador == "Tesoura":  # Verifica quem vai ganhar, perder ou empatar
        print("VOCÊ \033[031mPERDEU!")
    elif computador == "Tesoura" and jogador == "Papel":
        print("VOCÊ \033[031mPERDEU!")
    elif computador == "Papel" and jogador == "Pedra":
        print("VOCÊ \033[031mPERDEU!")
    elif computador == jogador:
        print("EMPATE!")
    else:
        print(emoji.emojize("VOCÊ \033[032mGANHOU! :tada:", language="alias"))
else:
    print(emoji.emojize("Não tente trapacear :angry:", language="alias"))
    print("Digite um valor valido na próxima")
