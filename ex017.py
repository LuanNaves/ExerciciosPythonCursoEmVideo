from math import hypot
cat_op = float(input("Comprimento do cateto oposto: "))
cat_ad = float(input("Comprimento do cateto adjascente: "))
hip = hypot(cat_ad, cat_op)
print(f"A hipotenusa desse triangulo retângulo é igual a {hip:.2f}")