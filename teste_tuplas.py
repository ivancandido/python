emails = ["ivan@gmail.com", "elaine@gmail.com"]
tupla = list(enumerate(emails))
print(tupla)

for chave in range(0, len(tupla)):
    print("chave: ", tupla[chave][0])
    print("valor: ", tupla[chave][1])
