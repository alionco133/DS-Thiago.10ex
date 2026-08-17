limite = int(input("informe um limite: "))
numero = 1
contador = 0

while numero <= limite:
    if numero % 2 == 0:
        contador += 1
    numero += 1

print("números pares:", contador)