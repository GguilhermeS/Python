import os

while True:
    os.system('cls')
    print ("Prograama de saber quem é o maior")

    n1 = float(input("Qual o primeiro numero?"))
    n2 = float(input("Qual o segundo numero?"))
    n3 = float(input("Qual o terceiro numero?"))

    if n1 == n2 == n3:
        print(f"Todos os números são iguais: {n1}")

    elif n1 >= n2 and n1 >= n3:
        print(f"O maior número entre {n1}, {n2}, {n3} é {n1}")
    elif n2 >= n1 and n2 >= n3:
        print(f"O maior número entre {n1}, {n2}, {n3} é {n2}")
    else:
        print(f"O maior número entre {n1}, {n2}, {n3} é {n3}")


    resposta = input("\nDeseja repetir o programa? (s/n): ").lower()
    if resposta != 's':
        print("Encerrando...")
        break
    
    
