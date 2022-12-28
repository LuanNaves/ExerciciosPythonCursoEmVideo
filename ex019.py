from random import choice
al1 = input("Primeiro aluno: ")
al2 = input("Segundo aluno: ")
al3 = input("Terceiro aluno: ")
al4 = input("Quarto aluno: ")
lista = [al4, al1, al3, al2]
escolhido = choice(lista)
print(f"O aluno escolhido foi {escolhido}")
