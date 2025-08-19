import random

def todos_os_caracteres():
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "!@#$%&*?"
    return letras + numeros + simbolos

def gerar_senha():
    while True:
        print("\n------ Menu -------")
        nova_senha = input("Gerar uma nova Senha? (S/N): ").strip().upper()

        if nova_senha != "S":
            print("Saindo...")
            break

        try:
            tamanho = int(input("Digite o tamanho da senha: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        incluir_letras = input("Incluir letras? (S/N): ").strip().upper() == "S"
        incluir_numeros = input("Incluir números? (S/N): ").strip().upper() == "S"
        incluir_simbolos = input("Incluir símbolos? (S/N): ").strip().upper() == "S"

        todos = ""
        if incluir_letras:
            todos += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if incluir_numeros:
            todos += "0123456789"
        if incluir_simbolos:
            todos += "!@#$%&*?"

        if not todos:
            print("Você precisa selecionar pelo menos um tipo de caractere!")
            continue

        senha = "".join(random.choice(todos) for _ in range(tamanho))
        print(f"Senha gerada: {senha}")

if __name__ == "__main__":
    gerar_senha()
