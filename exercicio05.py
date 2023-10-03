ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    if not fila:
        print("Fila vazia. Encerrando o atendimento.")
        break

    print(f"\nExistem {len(fila)} clientes na fila")
    print("Fila atual: ", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, A ou S): ")

    if operacao == "A":
        atendido = fila.pop(0)
        print(f"Cliente {atendido} atendido")
    elif operacao == "F":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == "S":
        print("Encerrando o atendimento.")
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")
