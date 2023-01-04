from time import sleep
import emoji

for cont in range(10, 0, -1):
    print(cont)
    sleep(1)
print(emoji.emojize(":fireworks: Feliz Ano Novo!!! :fireworks:", language="alias"))
