import os

mensagem = []

nome = input("Nome: ")

while True:

    os.system("cls")

    if len(mensagem) > 0:
        for x in mensagem:
            print(x['nome'], "_", x['texto'])

    print("_____________________")

    texto = input("mensagem: ")
    if texto == "fim":
        break

    mensagem.append({
        "nome": nome,
        "texto": texto
    })