distancia = float(input("Qual é a distância da viagem? "))
if distancia <= 200:
    print(f"Valor da passagem: R${distancia * 0.5:.2f}")
else:
    print(f"Valor da passagem: R${distancia * 0.45:.2f}")
