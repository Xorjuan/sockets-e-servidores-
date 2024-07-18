import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1", 65343))
# prepara a conexão
server_socket.listen(1)

print("servidor no aguardo na porta 65343")

# receber dados
while True:
    # aceita a conexão
    cliente_socket, cliente_endereço = server_socket.accept()
    print("conexão de {cliente_endereço} ")

    data = cliente_socket.recv(1024).encode()
    if not data:
        break
    print("recebido", data.decode())

    # envia resposta
cliente_socket.send("mensagem recebida".encode())

cliente_socket.close()
