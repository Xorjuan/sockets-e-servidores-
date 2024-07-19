import socket
import struct
from schemdraw.parsing import logicparse

BUFFER_SIZE = 64 * 1024  # 64 KB

def process_request(data):
    parts = data.split('|')
    question = int(parts[0])

    if question == 1:
        if parts[1] == 'hex':
            return convert_hex(parts[2])
        elif parts[1] == 'bin':
            return convert_bin(parts[2])
    elif question == 2:
        return operacao_binaria(parts[1], parts[2], parts[3])
    elif question == 3:
        return binary_division(parts[1], parts[2])
    elif question == 4:
        return float_to_ieee754(parts[1])
    elif question == 5:
        if parts[1] == 'ascii_to_hex':
            return word_to_hex(parts[2])
        elif parts[1] == 'utf8_compare':
            phrase1, phrase2 = parts[2], parts[3]
            bytes1 = phrase1.encode('utf-8')
            bytes2 = phrase2.encode('utf-8')
            return f"Frase 1: {len(bytes1)} bytes, hex: {bytes1.hex()}\nFrase 2: {len(bytes2)} bytes, hex: {bytes2.hex()}\nDiferença: {len(bytes2) - len(bytes1)} bytes"
    elif question == 6:
        logic_expr = parts[1]
        d = logicparse(logic_expr)
        d.save("image.jpg")
        with open("image.jpg", 'rb') as f:
            file_data = f.read()
        return file_data
    else:
        return "Questão inválida"

def start_server():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Servidor escutando em {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conectado por {addr}")
                while True:
                    data = conn.recv(BUFFER_SIZE).decode()
                    if not data:
                        break
                    response = process_request(data)
                    if isinstance(response, bytes):  # Check if response is binary data
                        # Send file size first
                        file_size = struct.pack('>I', len(response))
                        conn.sendall(file_size)
                        # Send file data
                        conn.sendall(response)
                    else:
                        conn.sendall(response.encode())

if __name__ == "__main__":
    start_server()
