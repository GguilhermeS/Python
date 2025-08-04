print("Programa de contagem de números primos")

numero = int(input("Digite um número inteiro: "))

quantidade = 0 

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(1, numero + 1):
    if eh_primo(i):
        quantidade += 1

print(f"\nExistem {quantidade} números primos entre 1 e {numero}.")
