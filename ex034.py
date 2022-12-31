salario = float(input("Digite o salário do funcionário: R$"))
if salario > 1250.00:
    aumento = salario * 10 / 100
else:
    aumento = salario * 15 / 100
print(f"O aumento será de R${aumento:.2f}")
print(f"Salário novo: R${salario + aumento:.2f}")
