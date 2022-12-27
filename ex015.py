dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valor_dias = dias * 60
valor_km = km * 0.15
print(f'Total a pagar: R${valor_km + valor_dias:.2f}')