print("-" * 22)
print("Sequência de Fibonacci")
print("-" * 22)
num = int(input("Quantos termos da sequência você quer ver? "))
num1 = 0
num2 = 1
num3 = 0
count = 0
print(f"Os {num} primeiros elementos da Sequencia de Fibonacci são: ")
while count < num:
    print(f"{num1} ->", end=" ")
    num3 = num1
    num1 = num2 + num1
    num2 = num3
    count += 1
print("FIM")
