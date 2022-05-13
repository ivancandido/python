from socket import *

servidor = "PANTHRO"
porta = 43210

msg = bytes(input("Digite algo: "), 'utf-8')
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor, porta))
obj_socket.send(msg)
#resposta como tamanho de 1024 bytes
resposta = obj_socket.recv(1024)
print("Recebemos: ", resposta)
obj_socket.close()