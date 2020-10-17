def teste():
    a = 0
    b = 1
    resposta = []
 
    for i in range(51):
        soma = b
        b = b + a
        a = soma

        resposta.append(b)
    return resposta

teste()
print(teste())