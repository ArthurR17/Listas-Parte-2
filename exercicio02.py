animais = ["Bingo", "Sabrino", "Kiko", "Princesa", "Bobby"]
p = input("Digite o nome do seu animal: ")
achou = False
x = 0

while x < len(animais):
    if animais[x] == p:
        achou = True
        break
    x += 1
if achou:
    print("Seu animal %s foi achado na posição %s" % (p, x))
else:
    print("Seu animal %s não foi encontrado" % p)

