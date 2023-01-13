while True:
    num = int(input("Quer ver a tabuada de qual número? "))
    if num < 0:
        break
    print('-' * 14)
    print(f"TABUADA DE {num}")
    print('-' * 14)
    for x in range(1, 11):
        print(f"{num} x {x:2} = {num * x}")
        x += 1
    print('-' * 14)
print("Programa TABUADA encerrado.")
