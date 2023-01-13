soma = 0
count = 0
while True:
    num = int(input("Digite um número inteiro (999 para parar): "))
    if num == 999:
        break
    count += 1
    soma += num
print(f"Foram digitados {count} números antes do número flag (999) ser digitado, e a soma deles foi {soma}")
