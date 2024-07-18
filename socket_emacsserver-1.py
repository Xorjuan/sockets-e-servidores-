import socket

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente_socket.connect(("127.0.0.1", 65343))

mensagem = "ola servidor"

cliente_socket.send(mensagem.encode())

data = cliente_socket.recv(1024)
print("recebido do servidor:", data.decode())

cliente_socket.close()
