numero = int(input("Digite um número: "))
soma = 0

while numero != 0:
    soma += numero
    numero = int(input("Digite um numero (0 para parar): "))

print("soma dos numeros é:", soma)