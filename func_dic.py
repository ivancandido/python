def perguntar():
    return input("Digite a opção desejada: \n" +
                 "<I> - para inserir um usuário \n" +
                 "<P> - para pesquisar um usuário \n" +
                 "<E> - para excluir um usuário \n" +
                 "<L> - para listar um usuário \n").upper()

def inseriruser(dicionario):
    dicionario[input("Digite o login: ")] = [input("Digite o nome: "), input("Digite o e-mail: "), input("Digite o nascimento: ")]
    salvar(dicionario)

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("######## EXIBINDO RESULTADO ##########")
        print("Nome.........:" + lista[0])
        print("E-mail.......:" + lista[1])
        print("Nascimento...:" + lista[2])
        print("######################################")
    else:
        print("######## USUÁRIO NÃO ENCONTRADO ##########")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("#### EXIBINDO ITENS ####")
        print("Login: ", chave,"\n")
        print("Dados: ", valor, "\n")

def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
        print("#### ITEM REMOVIDO ####")

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + " : " + str(valor))