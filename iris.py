basedados = []
with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        basedados = registro.split(",")
        print(basedados[0] + " - " + basedados[1] + " - " + basedados[2] + " - " + basedados[3] + " - " + basedados[4])