senha_correta = "244455555"
tentativas = 0
senha = ""

while senha != senha_correta and tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas += 1

if senha == senha_correta:
    print("liberado")
else:
    print("negado")