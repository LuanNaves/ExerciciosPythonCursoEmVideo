n1 = int(input("\033[34mDigite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: \033[m"))
opcao = 0
while opcao != 5:
    print("[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa")
    opcao = int(input("\033[34mEscolha uma opção: \033[m"))
    if opcao == 1:
        soma = n1 + n2
        print(f"\033[33m{n1}\033[m + \033[33m{n2}\033[m = \033[1;33m{soma}\033[m")
    elif opcao == 2:
        mult = n1 * n2
        print(f"\033[35m{n1}\033[m x \033[35m{n2}\033[m = \033[1;35m{mult}\033[m")
    elif opcao == 3:
        if n1 > n2:
            print(f"\033[36m{n1}\033[m é \033[35mMAIOR.\033[m")
        elif n2 > n1:
            print(f"\033[36m{n2}\033[m é \033[35mMAIOR\033[m")
        else:
            print(f"Os dois valores são \033[35mIGUAIS\033[m")
    elif opcao == 4:
        n1 = int(input("\033[34mDigite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: \033[m"))
    elif opcao == 5:
        print("PROGAMA FINALIZADO")
    else:
        print("\033[31mValor invalido\033[m")
        opcao = int(input("\033[34mEscolha uma opção: \033[m"))