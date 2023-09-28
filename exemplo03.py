l = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
achou = False
x = 0

while x < len(l):
    if l[x] == p:
        achou = True
        break
    x += 1
if achou:
    print("%d Achado na posição %d" % (p, x))
else:
    print("%d não encontrado" % p)