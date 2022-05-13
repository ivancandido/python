equipamento = []
valor = []
resposta = "S"

while resposta == "S":
    equipamento.append(input("Informe o nome do equipamento: "))
    valor.append(float(input("Infome o valor: ")))
    resposta = input("Deseja continuar S/N ?").upper()

#for indice in range(0, len(equipamento)):
#    print("Equipamento.....: ", equipamento[indice])
#    print("Valor...........: ", valor[indice])

busca = input("Qual equipamento deseja?")
for indice in range(0, len(equipamento)):
    if busca == equipamento[indice]:
        print("Achei o ", equipamento[indice])
        print("O valor é: ", str(valor[indice]))