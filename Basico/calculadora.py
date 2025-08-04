while True:
    print ("Calculadora")

    n1 = int(input("Qual o primeiro numero? "))

    n2 = int(input("Qual o segundo numero? "))

    print (input("Qual operação deseja utilizar: \n1.Adição \n2.Subtração \n3.Divisão \n4.Multiplicação \n5.Raiz Quadrada"))
    resp = int(input("Resposta:"))


    if resp == 0:
        print("Saindo...")
        break
    elif resp < 1 or resp > 5:
            print("Escolha uma operação válida.")
    elif resp == 1:
        adicao = n1 + n2
        print("A soma dos numero ",n1, " e ", n2, "é de: ", adicao )
    elif resp == 2:
        subtracao = n1 - n2
        print("A subtração dos numero ",n1, " e ", n2, "é de: ", subtracao )
    elif resp == 3:
        divisao = n1 / n2
        print("A divisão dos numero ",n1, " e ", n2, "é de: ", divisao )
    elif resp == 4:
        multiplicacao = n1 + n2
        print("A multiplicação dos numero ",n1, " e ", n2, "é de: ", multiplicacao )
    elif resp == 5:
        raiz = n1 * n1
        raiz2 = n2 * n2
        print("A raiz quadrada dos numero ",n1, " e ", n2, "é de:", raiz ,"e", raiz2 )
    else:
        print ("gwajrfgwqg")