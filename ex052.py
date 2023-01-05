num = int(input("Digite um número: "))
mult = 0
for x in range(2, num):
    if num % x == 0:
        mult += x
if mult == 0:
    print(f"O número {num} é PRIMO")
else:
    print(f"O número {num} NÃO é PRIMO")
