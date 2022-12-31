reta1 = float(input("Informe o valor da primeira reta: "))
reta2 = float(input("Informe o valor da segunda reta: "))
reta3 = float(input("Informe o valor da terceira reta: "))
if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta2 + reta1:
    print("Essas 3 retas podem formar um triângulo.")
else:
    print("Essas 3 retas não podem formar um triangulo.")
