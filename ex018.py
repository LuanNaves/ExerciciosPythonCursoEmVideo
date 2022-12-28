import math
angulo = float(input("Digite um ângulo: "))
math.radians(angulo)
print(f"O ângulo de {angulo} tem o SENO de {math.sin(math.radians(angulo)):.2f}, o COSENO de {math.cos(math.radians(angulo)):.2f} e a TANGENTE de {math.tan(math.radians(angulo)):.2f}")
