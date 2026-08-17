saldo = float(input("Digite o saldo inicial: "))

while saldo > 0:
    valor = float(input("Digite o valor do saque: "))

    if valor <= saldo:
        saldo -= valor
        print("Saque realizado!")
        print("Saldo atual:", saldo)
    else:
        print("Saldo insuficiente!")

print("Saldo zerado ou negativo.")