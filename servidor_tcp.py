from socket import *

servidor = "PANTHRO"
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor, porta))
obj_socket.listen(2)

print("Aguardando cliente")

while True:
    conn, cliente = obj_socket.accept()
    print("Conectado com:", cliente)
    while True:
        msg_recebida = str(conn.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Ola Cliente'
        conn.send(msg_enviada)
        break
    conn.close()
