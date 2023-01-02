print("-=" * 14)
print("Conversor de número decimal")
print("-=" * 14)
num = int(input("Digite um número: "))
print("Qual será a base de conversão? Para escolher digite:")
print("""1 - Para converter para BINÁRIO
2 - Para converter para OCTAL
3 - Para converter para HEXADECIMAL""")
base = int(input("Sua escolha: "))
if base == 1:
    print(f"A representação em binário do número {num} é {bin(num)[2:]}.")
elif base == 2:
    print(f"A representação em octal do número {num} é {oct(num)[2:]}.")
elif base == 3:
    print(f"A representação em hexadecimal do número {num} é {hex(num)[2:]}.")
else:
    print("Você não digitou um valor valido para a base e conversão.")
    print("Tente novamente.")
