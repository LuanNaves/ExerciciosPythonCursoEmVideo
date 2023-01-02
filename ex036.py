valor_da_casa = float(input("Qual o valor da casa que você deseja comprar? R$"))
salario = float(input("Qual é o seu salário? R$"))
anos = int(input("Em quantos anos você pretende pagar a casa? "))
valor_prestacao = valor_da_casa / (anos * 12)
if valor_prestacao <= salario * 30 / 100:
    print(f"Você pode comprar essa casa.")
    print(f"O valor de cada prestação será de R${valor_prestacao:.2f}")
else:
    anos = valor_da_casa / ((salario * 30 / 100) * 12)
    print("Infelizmente, com essas condições não será possivel a compra dessa casa.")
    print("O valor de cada prestação deve ser de no máximo 30% do salário")
    print(f"Seria possível a compra se estiver disposto a parcelar por {anos.__ceil__()} anos")

