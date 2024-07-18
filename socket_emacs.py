# uso da bibloteca sockets

import socket


# define o para qual endereço que ira se conectar
def start_client():
    host = "127.0.0.1"
    port = 65432
    # cria o scoket para ser o cliente e definindo padroes como qual protocolo ira usar e qual tipo enderecamento ira usar
    # está offiline
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # se conecta ao servidor que está no aguardo
            # online
            s.connect((host, port))
            print(f"Conectado ao servidor em {host}:{port}")

            while True:
                message = input("Digite uma mensagem (ou 'sair' para encerrar): ")
                if message.lower() == "sair":
                    break
                # envia a mensagem e codifica em um padrão universal
                s.sendall(message.encode())
                # define o padraão do limite de bits que será a mensagem de retorno
                data = s.recv(1024)
                print(f"Resposta do servidor: {data.decode()}")
        # online..... mas confirmar com o professor
        # retorna caso o servidor esteja offiline
        except ConnectionRefusedError:
            print(
                "Não foi possível conectar ao servidor. Verifique se ele está online."
            )


if __name__ == "__main__":
    start_client()
