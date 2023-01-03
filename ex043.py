print("\033[35mCALCULADOR DE IMC\033[m")
altura = float(input("Qual é a sua altura (em metros)? "))
peso = float(input("Qual é o seu peso (em kg)? "))
imc = peso / pow(altura, 2)
print(f"Seu IMC é de {imc:.1f}")
if imc < 18.5:
    print("Status: ABAIXO DO PESO.")
elif 18.5 <= imc < 25:
    print("Status: PESO IDEAL")
elif 25 <= imc < 30:
    print("Status: SOBREPESO")
elif 30 <= imc < 40:
    print("Status: OBESIDADE")
else:
    print("Status: OBESIDADE MÓRBIDA")
