from socket import *

servidor = "PANTHRO"
porta = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((servidor, porta))
saida = ""

while saida != "X":
    msg = input("Sua mensagem: ")
    obj_socket.sendto(msg.encode(), (servidor, porta))
    dados, mensagem = obj_socket.recvfrom(65535)
    print("Resposta do servidor: ", dados.decode())
    saida = input("Digite <X> para sair: ").upper()

obj_socket.close()