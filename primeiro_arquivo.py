arquivo = open("file1.txt", "w")
arquivo.write("Meu primeiro arquivo...")
arquivo.close()

with open("file1.txt", "a") as arquivo:
    arquivo.write("teste")

with open("file1.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open("file1.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(">> ", linha)