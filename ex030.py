num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"O número {num} é \033[1;34mPAR\033[m.")
else:
    print(f"O número {num} é \033[1;34mÍMPAR\033[m.")
