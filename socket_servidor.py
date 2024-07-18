import socket

# endereço e a porta do servidor
host = "localhost"
port = 6543

# define a variavel server para receber o tipo de protocolo
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # offline
# chamamos o blind para usar nosso local host e nossa porta
server.bind((host, port))  # online

print("aguardando conexão de um cliente ")
# o comm está esperando a função server aceitar um endereço

server.listen(1)  # o servidor aceita apenas um cliente
conn, ender = server.accept()

print("conecatdo em ", ender)

while True:
    # conn consegue receber dados com até 2048 bytes
    data = conn.recv(2048)
    if not data:
        # usamos o not para verficar se temos dados em conn
        print("fechando a conexão ")
        conn.close()
        break
    # usamos o sendall para retornar os dados que o cliente enviou como
    # confirmação que recebemos os dados
    conn.sendall(data)
