import socket
import sys


def send_request(question, *args, host="127.0.0.1", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        request = f"{question}|{'|'.join(args)}"
        s.sendall(request.encode())
        response = s.recv(1024).decode()
    return response


# All other functions (print_utf8_table, print_ascii_table) remain unchanged


def main_menu(host, port):
    while True:
        print("\nEscolha uma questão:")
        print("1. Conversão Hexadecimal/Binário")
        print("2. Operação Binária")
        print("3. Divisão Binária")
        print("4. Conversão para IEEE 754")
        print("5. ASCII para Hexadecimal e UTF-8")
        print("6. Sair")

        choice = input("Digite o número da questão desejada: ")

        if choice == "1":
            sub_choice = input("Escolha 'hex' para hexadecimal ou 'bin' para binário: ")
            value = input("Digite o valor para conversão: ")
            result = send_request(1, sub_choice, value, host=host, port=port)
            print(f"Resultado: {result}")

        # Other elif blocks remain the same, just add host=host, port=port to send_request calls

        elif choice == "6":
            print("Encerrando o programa...")
            sys.exit(0)

        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python socket_cliente2.py <endereço_ip> <porta>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    print(f"Conectando ao servidor em {host}:{port}")
    main_menu(host, port)
