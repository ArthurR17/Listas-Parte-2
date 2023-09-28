print("-" * 50)
print("%15s LISTA DOS PRODUTOS" % " ")
print("-" * 50)
print("%1sCÓDIGO" % " ", "%10sPRODUTO" % " ")
print("-" * 50)
print("%1s0" % " ", "%10sRação Aracanine para cães adultos" % " ")
print("%1s1" % " ", "%10sSemente de girassol Viridian" % " ")
print("%1s2" % " ", "%10sRação Meowth para gatos filhotes" % " ")
print("%1s3" % " ", "%10sBiscoito Persian" % "")
print("%1s4" % " ", "%10sRação Ratata para hamster" % " ")
print("%1s5" % " ", "%10sAlimento para peixes Magikarp" % " ")
print("-" * 50)

produtos = ["Ração Aracanine para cães adultos", "Semente de girassol Viridian", "Ração Meowth para gatos filhotes", "Biscoito Persian", "Ração Ratata para hamster", "Alimento para peixes Magikarp"]

codigo = int(input("Digite o código do produto: "))

if codigo == 0:
    print(f"Você pediu o produto {produtos[0]}")
elif codigo == 1:
    print(f"Você pediu o produto {produtos[1]}")
elif codigo == 2:
    print(f"Você pediu o produto {produtos[2]}")
elif codigo == 3:
    print(f"Você pediu o produto {produtos[3]}")
elif codigo == 4:
    print(f"Você pediu o produto {produtos[4]}")
elif codigo == 5:
    print(f"Você pediu o produto {produtos[5]}")
else:
    print("Código inválido!")
