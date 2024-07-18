import socket

# usando como cliente o endereço IP do computador
host = '127.0.0.1'
port = 6543
# lembrando que a porta precisa ser a mesma se não vai funcionar
# usamos a familia de protocolos ipv4
# parte offline
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# fazemos a conexão com a porta e o host
cliente.connect((host, port))

# para enviar os dados para o servidor
# importante codificar em string para o servidor
cliente.sendall(str.encode("ola servidor "))
# definimos o tamanho da mensagem que podemos trabalhar
data = cliente.recv(2048)
# exibimos a mensagem do servidor e usamos o decode para forçar a saida em litte-endian
print("mensagem do servidor", data.decode())
