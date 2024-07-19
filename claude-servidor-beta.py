import socket
import struct
from schemdraw.parsing import logicparse
import os

BUFFER_SIZE = 64 * 1024  # 64 KB

def handle_client_connection(conn):
    while True:
        data = conn.recv(BUFFER_SIZE).decode()
        if not data:
            break
        
        # Split the request into components
        request_parts = data.split('|')
        question = int(request_parts[0])
        args = request_parts[1:]

        if question == 1:
            # Handle Hex/Bin conversion
            sub_choice = args[0]
            value = args[1]
            if sub_choice == 'hex':
                response = hex(int(value, 2))[2:]
            elif sub_choice == 'bin':
                response = bin(int(value, 16))[2:]
            else:
                response = "Opção inválida para conversão."
            conn.sendall(response.encode())

        elif question == 2:
            # Handle Binary Operation
            bin1 = args[0]
            bin2 = args[1]
            op = args[2]
            try:
                int_bin1 = int(bin1, 2)
                int_bin2 = int(bin2, 2)
                if op == '+':
                    result = bin(int_bin1 + int_bin2)[2:].zfill(8)
                elif op == '-':
                    result = bin(int_bin1 - int_bin2)[2:].zfill(8)
                else:
                    result = "Operação inválida."
            except ValueError:
                result = "Entrada inválida para operação binária."
            conn.sendall(result.encode())

        elif question == 3:
            # Handle Binary Division
            dividendo = args[0]
            divisor = args[1]
            try:
                int_dividendo = int(dividendo, 2)
                int_divisor = int(divisor, 2)
                result = bin(int_dividendo // int_divisor)[2:]
            except ValueError:
                result = "Entrada inválida para divisão binária."
            conn.sendall(result.encode())

        elif question == 4:
            # Handle IEEE 754 Conversion
            num = float(args[0])
            response = format(num, '.10e')
            conn.sendall(response.encode())

        elif question == 5:
            # Handle ASCII/UTF-8 Conversion
            option = args[0]
            if option == "ascii_to_hex":
                word = args[1]
                result = ''.join(f"{ord(c):02X}" for c in word)
            elif option == "utf8_compare":
                phrase1 = args[1]
                phrase2 = args[2]
                result = f"Comparando '{phrase1}' com '{phrase2}' em UTF-8"
            else:
                result = "Opção inválida para conversão ASCII/UTF-8."
            conn.sendall(result.encode())

        elif question == 6:
            # Handle Logic Diagram Generation
            logic_expr = " and ".join(args)
            try:
                d = logicparse(logic_expr)
                d.save("logic_diagram.jpg")

                # Send the file size and file data
                file_size = os.path.getsize("logic_diagram.jpg")
                conn.sendall(struct.pack('>I', file_size))
                with open("logic_diagram.jpg", 'rb') as f:
                    while chunk := f.read(BUFFER_SIZE):
                        conn.sendall(chunk)
            except Exception as e:
                conn.sendall(f"Erro ao gerar o diagrama lógico: {e}".encode())

        elif question == 7:
            # Handle Logical Expression Generation
            params = args
            if len(params) >= 5:
                result = "Parâmetros demais!"
            else:
                expr = concat_params(params)
                if expr != "Parâmetros demais!":
                    try:
                        d = logicparse(expr)
                        d.save("generated_expression.jpg")
                        
                        # Send the file size and file data
                        file_size = os.path.getsize("generated_expression.jpg")
                        conn.sendall(struct.pack('>I', file_size))
                        with open("generated_expression.jpg", 'rb') as f:
                            while chunk := f.read(BUFFER_SIZE):
                                conn.sendall(chunk)
                        result = "Expressão lógica gerada e salva como generated_expression.jpg"
                    except Exception as e:
                        result = f"Erro ao gerar a expressão lógica: {e}"
                else:
                    result = "Parâmetros inválidos."
            conn.sendall(result.encode())

        else:
            conn.sendall("Questão inválida.".encode())

    conn.close()

def concat_params(args):
    if len(args) >= 5:
        return "Parâmetros demais!"
    else:
        params = list(args)
        while len(params) < 4:
            params.append(str(1))
        return " and ".join(params)

def start_server():
    host = "25.0.111.214"
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Servidor ouvindo em {host}:{port}...")

        while True:
            conn, addr = server_socket.accept()
            print(f"Conectado por {addr}")
            handle_client_connection(conn)

if __name__ == "__main__":
    start_server()
