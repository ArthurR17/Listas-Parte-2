visitas = []
while True:
    produto = input("Digite 1 para marcar que você visitou o site ou 0 para sair: ")
    if produto == "0":
        break
    visitas.append(produto)

for e in visitas:
    print(f"Você visitou o site {visitas.count('1')} vezes")
    break

