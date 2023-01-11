num = int(input("Digite um número inteiro (999 para parar): "))
soma = 0
count = 0
while num != 999:
    count += 1
    soma += num
    num = int(input("Digite um número inteiro: "))
print(f"Foram digitados {count} números antes do número flag (999) ser digitado, e a soma deles foi {soma}")
