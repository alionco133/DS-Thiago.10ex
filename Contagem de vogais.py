palavra = input("Digite uma palavra: ")
indice = 0
quantidade = 0

while indice < len(palavra):
    if palavra[indice].lower() in "aeiou":
        quantidade += 1
    indice += 1

print("Quantidade de vogais:", quantidade)