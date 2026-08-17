soma = 0
quantidade = 0

nota = float(input("Digite uma nota (0 a 10): "))

while nota >= 0:
    if nota <= 10:
        soma += nota
        quantidade += 1
    else:
        print("Nota invalida!")

    nota = float(input("digite outra nota (0 a 10): "))

if quantidade > 0:
    media = soma / quantidade
    print("Média:", media)
else:
    print("nenhuma nota valida foi digitada")