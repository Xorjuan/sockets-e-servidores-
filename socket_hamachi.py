import socket

# Criação do socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexão ao servidor
server_address = ('25.0.111.214', 65432)
print(f"Connecting to {server_address[0]} port {server_address[1]}")
client_socket.connect(server_address)

try:
    # Enviando dados
    message = 'This is the message. It will be repeated.'
    print(f"Sending {message}")
    client_socket.sendall(message.encode())

    # Procurando a resposta
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = client_socket.recv(16)
        amount_received += len(data)
        print(f"Received {data}")

finally:
    print("Closing socket")
    client_socket.close()
