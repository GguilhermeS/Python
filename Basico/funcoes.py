fluxo_caixa = []

print("-----------------------------")
print("Fluxo caixa")
print("-----------------------------")
print("1 - Adicionar receita")
print("2 - Adicinar despesa")
print("\n# Digite outro valor para sair #\n")

def adicionar_transacao():
        nome = input("Nome: ")
        valor = float(input("Valor: "))
        fluxo_caixa.append({
            "nome":nome,
            "valor":valor
        })


while True:

    op = int(input("Digite a opção: "))

    if op == 1:
        adicionar_transacao()
    elif op == 2:
        adicionar_transacao()
    else:
        break
total = 0
for fc in fluxo_caixa:
    print("Nome: ", fc['nome'], "Valor: ", fc['valor'])
    total = total + fc['valor']

print("Saldo atual: R$", total )