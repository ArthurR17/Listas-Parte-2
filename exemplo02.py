prato = 5
pilha = list(range(1, prato + 1))

while True:
    print(f"\nExistem %d pratos na pilha  " % len(pilha))
    print("Pilha atual: ", pilha)
    print("Digite E para adicionar um prato ao fim da pilha,")
    print("ou D para desempilhar. S para sair.")
    operacao = input("Operação (E, D ou S): ")
    if operacao == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print("Prato %d removido" % lavado)
        else:
            print("Pilha vazia! Nada para lavar.")
    elif operacao == "E":
        prato += 1
        pilha.append(prato)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas E, D ou S!")