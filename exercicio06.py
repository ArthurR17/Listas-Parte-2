
estoque = ["Banana", "Maçã", "Laranja", "Abacaxi", "Manga"]
estoque[0] = 5
estoque[1] = 8
estoque[2] = 3
estoque[3] = 7
estoque[4] = 2

print("-" * 50)
print("%15s LISTA DOS PRODUTOS" % " ")
print("-" * 50)
print("%1sCÓDIGO" % " ", "%10sPRODUTO" % " ", "%10sQUANTIDADE" % " ")
print("-" * 50)
print("%1sB" % " ", "%15sBanana" % " ", "%15s5" % " ")
print("%1sM" % " ", "%15sMaça" % " ", "%17s8" % " ")
print("%1sL" % " ", "%15sLaranja" % " ", "%14s3" % " ")
print("%1sA" % " ", "%15sAbacaxi" % "", "%14s7" % " ")
print("%1sM" % " ", "%15sManga" % " ", "%16s2" % " ")
print("-" * 50)

codigo = input("Digite a letra inicial do produto que deseja remover: ")

while True:
    if codigo == "0":
        break
    for e in codigo:
        if e == "B":
            estoque[0] -= 1
            print(f"Você removeu 1 Banana do estoque, agora restam apenas {estoque[0]} bananas")
            codigo = input("Digite a letra inicial do produto que deseja remover: ")
        elif e == "M":
            estoque[1] -= 1
            print(f"Você removeu 1 Maçã do estoque, agora restam apenas {estoque[1]} maçãs")
            codigo = input("Digite a letra inicial do produto que deseja remover: ")
        elif e == "L":
            estoque[2] -= 1
            print(f"Você removeu 1 Laranja do estoque, agora restam apenas {estoque[2]} laranjas")
            codigo = input("Digite a letra inicial do produto que deseja remover: ")
        elif e == "A":
            estoque[3] -= 1
            print(f"Você removeu 1 Abacaxi do estoque, agora restam apenas {estoque[3]} abacaxis")
            codigo = input("Digite a letra inicial do produto que deseja remover: ")
        elif e == "M":
            estoque[4] -= 1
            print(f"Você removeu 1 Manga do estoque, agora restam apenas {estoque[4]} mangas")
            codigo = input("Digite a letra inicial do produto que deseja remover: ")
        else:
            print("Código inválido!")
            codigo = input("Digite a letra inicial do produto que deseja remover: ")



