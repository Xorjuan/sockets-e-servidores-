import socket


def setup_client(host="25.0.111.214", port=65432):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s


def run_client():
    try:
        client_socket = setup_client()
        messages = [
            "1|hex|0x1F",
            "1|bin|111",
            "2|00000001|00000001|+",
            "3|00001000|00000010",
            "4|3.14",
            "5|ascii_to_hex|Hello",
            "5|utf8_compare|Olá|Hello",
        ]
        for message in messages:
            print(f"Enviando: {message}")
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Recebido: {data.decode()}")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    run_client()
