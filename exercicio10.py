
estoque = ["Banana", "Maçã", "Laranja", "Abacaxi", "Manga"]
estoque[0] = 12
estoque[1] = 8
estoque[2] = 6
estoque[3] = 3
estoque[4] = 9

print("-" * 70)
print("%15s LISTA DOS PRODUTOS" % " ")
print("-" *70)
print("%1sCÓDIGO" % " ", "%10sPRODUTO" % " ", "%30sQUANTIDADE" % " ")
print("-" * 70)
print("%1s1" % " ", "%10sRação Aracanine para cães adultos" % " ", "%12s12" % " ")
print("%1s2" % " ", "%10sSemente de girassol Viridian" % " ", "%17s08" % " ")
print("%1s3" % " ", "%10sRação Meowth para gatos filhotes" % " ", "%13s06" % " ")
print("%1s4" % " ", "%10sBiscoito Persian" % "", "%29s03" % " ")
print("%1s5" % " ", "%10sRação Ratata para hamster" % " ", "%20s02" % " ")
print("-" * 70)


codigo = input("Digite o código do produto que deseja remover (digite 0 para sair): ")

while True:
    if codigo == "0":
        print("-" * 70)
        print("%15s NOVA LISTA DOS PRODUTOS" % " ")
        print("-" * 70)
        print("%1sCÓDIGO" % " ", "%10sPRODUTO" % " ", "%30sQUANTIDADE" % " ")
        print("-" * 70)
        print("%1s1" % " ", "%10sRação Aracanine para cães adultos" % " ", f"%12s{estoque[0]}" % " ")
        print("%1s2" % " ", "%10sSemente de girassol Viridian" % " ", f"%17s{estoque[1]}" % " ")
        print("%1s3" % " ", "%10sRação Meowth para gatos filhotes" % " ", f"%13s{estoque[2]}" % " ")
        print("%1s4" % " ", "%10sBiscoito Persian" % "", f"%29s{estoque[3]}" % " ")
        print("%1s5" % " ", "%10sRação Ratata para hamster" % " ", f"%20s{estoque[4]}" % " ")
        print("-" * 70)
        break
    for e in codigo:
        if e == "1":
            estoque[0] -= 1
            print(f"Você removeu 1 Ração Aracaine do estoque, agora restam apenas {estoque[0]} rações")
            codigo = input("Digite a letra inicial do produto que deseja remover: ")
        elif e == "2":
            estoque[1] -= 1
            print(f"Você removeu 1 Semente de girassol, agora restam apenas {estoque[1]} sementes")
            codigo = input("Digite a letra inicial do produto que deseja remover: ")
        elif e == "3":
            estoque[2] -= 1
            print(f"Você removeu 1 Ração Meowth, agora restam apenas {estoque[2]} rações")
            codigo = input("Digite a letra inicial do produto que deseja remover: ")
        elif e == "4":
            estoque[3] -= 1
            print(f"Você removeu 1 Biscoito Persian, agora restam apenas {estoque[3]} biscoitos")
            codigo = input("Digite a letra inicial do produto que deseja remover: ")
        elif e == "5":
            estoque[4] -= 1
            print(f"Você removeu 1 Ração Ratata, agora restam apenas {estoque[4]} rações")
            codigo = input("Digite a letra inicial do produto que deseja remover: ")
        else:
            print("Código inválido!")
            codigo = input("Digite a letra inicial do produto que deseja remover: ")



