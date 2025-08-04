print ("Programa Cinema")

ingresso = int(input("Quantos ingressos existem?"))
compradores = int(input("Quantos compradores são estimados?"))

validacao = (ingresso >= compradores)

if ingresso > compradores:
    print ("Ingressos suficientes")
else:
        print("Não há ingressos suficientes")