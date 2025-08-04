notas = []

contador = 1

while contador <= 5:
    cod_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [cod_aluno, nota]
    notas.append(resultado)

    contador = contador + 1

for x in notas:
    cod_aluno = [0]
    nota = x[1]
    print ("A nota do aluno ", cod_aluno, "foi de ", nota)