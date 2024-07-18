import socket


def send_request(choice):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 65432)
    client_socket.connect(server_address)

    try:
        client_socket.sendall(choice.encode())
        response = client_socket.recv(4096).decode()
        print(f"Resposta do servidor: {response}")
    finally:
        client_socket.close()


def main():
    while True:
        print("\nEscolha uma questão:")
        print("1. Converter Hexadecimal e Binário")
        print("2. Operações Binárias")
        print("3. Divisão Binária")
        print("4. Conversão IEEE 754")
        print("5. Conversão e Comparação ASCII/UTF-8")
        print("6. Sair")

        choice = input("Digite o número da opção desejada: ")

        if choice == "6":
            send_request(choice)
            break
        else:
            send_request(choice)


if __name__ == "__main__":
    main()
