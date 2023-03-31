count = preco_mais_barato = mais_de_mil = total_preco = 0
nome_mais_barato = ""
print("-" * 26)
print("SUPERMERCADO DO LUAN")
print("-" * 26)
while True:
    count += 1
    nome = str(input("Nome do produto: ")).strip().capitalize()
    preco = float(input("Preço do produto: R$"))
    total_preco += preco
    if preco > 1000:
        mais_de_mil += 1
    if count == 1:
        preco_mais_barato = preco
        nome_mais_barato = nome
    else:
        if preco < preco_mais_barato:
            preco_mais_barato = preco
            nome_mais_barato = nome
    while True:
        continuar = str(input("Continuar? [S/N] ")).strip().upper()[0]
        if continuar in "SN":
            break
    if continuar == "N":
        print("-" * 26)
        break
print(f"O total da compra foi de R${total_preco:.2f}")
print(f"O produto mais barato foi {nome_mais_barato} que custa R${preco_mais_barato:.2f}")
print(f"Temos {mais_de_mil} produtos que custam mais de mil reais.")

