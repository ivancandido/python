from dicionarios.func_dic import *
usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inseriruser(usuarios)
    if opcao == "P":
        pesquisar(usuarios, input("Informe o login: "))
    if opcao == "E":
        excluir(usuarios, input("Iinforme o login: "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()