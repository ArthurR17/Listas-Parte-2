compras = []
while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    compras.append(produto)

for e in compras:
    print(f"Você escolheu os produtos: {compras}")
    break

