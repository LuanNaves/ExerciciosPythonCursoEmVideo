vel = int(input("Qual é a velocidade atual do carro? "))
if vel > 80:
    print("\033[1;31mMultado! Você passou do limite de velocidade que é 80km/h")
    print(f"Valor da multa: \033[1;33mR${7 * (vel - 80):.2f}")
print("\033[32mDirija com segurança e tenha um bom dia!")
