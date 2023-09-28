v = [9, 8, 7, 12, 6, 13, 21]
p = []
t = []

for e in v:
    if e % 2 == 0:
        p.append(e)
    else:
        t.append(e)

print("Pares: ", p)
print("Ímpares: ", t)