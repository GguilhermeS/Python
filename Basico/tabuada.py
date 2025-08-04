import os

while True:
    os.system('cls')

    print("Programa Tabuada")

    try:
        numero = float(input("Qual número deseja saber a tabuada? "))
    except ValueError:
        print("Por favor, digite um número válido.")
        input("Pressione ENTER para tentar novamente...")
        continue

    print(f"\nTabuada do {numero}:\n")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

    resposta = input("\nDeseja ver outra tabuada? (s/n): ").lower()
    if resposta != 's':
        print("Encerrando o programa.")
        break