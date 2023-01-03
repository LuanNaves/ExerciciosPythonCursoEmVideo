preco = float(input("Qual é o preço do produto? R$"))
print("FORMAS DE PAGAMENTO")
print("1 - À vista no Dinheiro/Cheque (10% de desconto)")
print("2 - À vista no Cartâo (5% de desconto)")
print("3 - Dividido em 2x no Cartâo sem juros")
print("4 - Dividido em 3x ou mais no Cartão com 20% de juros")
pagamento = int(input("Escolha a forma de pagamento digitando o número referente a ela: "))
if pagamento == 1:
    print(f"Preço a pagar: R${preco * 90 / 100:.2f}")
elif pagamento == 2:
    print(f"Preço a pagar: R${preco * 95 / 100:.2f}")
elif pagamento == 3:
    print(f"Preço a pagar: R${preco:.2f}")
    print(f"Valor de cada parcela: R${preco / 2:.2f}")
elif pagamento == 4:
    parcelas = int(input("Parcelar em quantas vezes? "))
    preco = preco * 120 / 100
    print(f"Preço a pagar: R${preco:.2f}")
    print(f"Valor de cada parcela: R${preco / parcelas:.2f}")
else:
    print("Opção inválida de forma de pagamento.")
