numero_secreto = 38
tentativa = int(input("tente adivinhar o número: "))
while tentativa != numero_secreto:
    if tentativa < numero_secreto:
        print("O número secreto é maior")
    else:
        print("O número secreto é menor")
    tentativa = int(input("Tente novamente: "))
print("parabéns vc acertou")