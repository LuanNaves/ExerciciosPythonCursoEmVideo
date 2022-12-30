import random
from time import sleep
num = random.randint(0, 5)
print("\033[1;35m=-" * 9 + "=")
print("\033[34mJOGO DA ADVINHAÇÃO")
print("\033[1;35m=-" * 9 + "=")
aposta = int(input("\033[mTente advinhar o numero de 0 a 5: "))
print("\033[34mSORTEANDO...\033[m")
sleep(2)
print(f"Número sorteado: {num}")
if num == aposta:
    print("\033[32mPARABÊNS, VOCÊ ACERTOU")
else:
    print("\033[31mVocê errou.\033[m Mais sorte na próxima!")
