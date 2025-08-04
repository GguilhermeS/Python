import os

print ("Programa de contagem")

palavra = input("Qual a sua palavra?: ")
palavra = palavra.lower()

vogais = "aeiou"

quantidade = 0

for l in palavra:
    if l in vogais:
        quantidade += 1

print(f"\nA Frase contem {quantidade} vogal(is)")

