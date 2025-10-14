import random

print ("Jogo da adivinhação")

numero_secreto = random.randint(1,10)

tentativa = 0
acertou = False

while not acertou:
    palpite = int(input("Digite o numero: "))
    tentativa += 1

    if tentativa == 5:
        print(f"Fim de jogo! Você não acertou. O número era {numero_secreto}.")
        break

    if palpite == numero_secreto:
        print(f"Parabens Vey o numero era {numero_secreto} em {tentativa}")
        acertou = True
    elif palpite < numero_secreto:
        print("O numero é maior")
    else:
        print("O numero é menor")