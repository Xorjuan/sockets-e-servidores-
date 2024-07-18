import socket


HOST = "192.168.15.14"  # endereço do servidor
PORT = 12345  # porta do servidor


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect((HOST, PORT))


message = "Olá, servidor!"
client_socket.sendall(message.encode("utf-8"))


data = client_socket.recv(1024).decode("utf-8")
print(f"Resposta do servidor: {data}")


client_socket.close()
