cidade = str(input("Qual cidade você nasceu? ")).strip().title()
separado = cidade.split()
santo = bool("Santo" in separado[0])
print(santo)
