import random
import emoji
from time import sleep
computador = random.randint(0, 10)
tentativas = 1
print("\033[1;35m=-" * 9 + "=")
print("\033[34mJOGO DA ADVINHAÇÃO")
print("\033[1;35m=-" * 9 + "=")
sleep(0.75)
print(emoji.emojize("\033[m:computer: - Vou pensar em um número de 0 a 10.", language="alias"))
sleep(1.5)
print(emoji.emojize("\033[34m:computer::thought_balloon: - PENSANDO...\033[m", language="alias"))
sleep(2)
aposta = int(input(emoji.emojize("\033[m:computer: - Tenta adivinhar: ", language="alias")))
while computador != aposta:
    print("\033[31mVocê errou.", end=" ")
    if computador > aposta:
        print(emoji.emojize("\033[mUm pouco mais... :wink:", language="alias"))
    if computador < aposta:
        print(emoji.emojize("\033[mPassou :laughing: Um pouco menos... ", language="alias"))
    aposta = int(input("\033[mTenta de novo: "))
    tentativas += 1
print("\033[32mPARABÊNS, VOCÊ ACERTOU\033[m")
if tentativas == 1:
    print(f"INCRÍVEL!! Você só precisou de uma tentativa para acertar.")
elif tentativas < 4:
    print(f"Muito bom! Você conseguiu acertar em {tentativas} tentativas.")
elif tentativas < 8:
    print(f"Nada mal. Você precisou de {tentativas} tentativas para acertar")
else:
    print(f"Que azar. Você precisou de {tentativas} tentativas para acertar.")
