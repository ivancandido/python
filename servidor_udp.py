from socket import *

servidor = "PANTHRO"
porta = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((servidor, porta))
print("Servidor pronto...")

while True:
    # range maximo de porta
    dados, origem = obj_socket.recvfrom(65535)
    print("Origem............: ", origem)
    print("Dados recebidos...: ", dados.decode()) #decodifica a mensagem recebida em bytes
    resposta = input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem) #codifica a mensagem para ser enviada

obj_socket.close()