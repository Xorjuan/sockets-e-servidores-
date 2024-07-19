import socket
import logging

# Configuração do logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def setup_client(question, *args):
    host = "25.0.111.214"
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        request = f"{question}|{'|'.join(args)}"
        s.sendall(request.encode())
        response = s.recv(1024).decode()
    return response


def run_client():
    client_socket = setup_client()
    try:
        messages = ["Hello, Server!", "How are you?", "Goodbye!"]
        for message in messages:
            logger.debug(f"Sending message: {message}")
            client_socket.sendall(message.encode())

            data = client_socket.recv(1024)
            logger.debug(f"Received data: {data.decode()}")
    except Exception as e:
        logger.error(f"Exception: {e}")
    finally:
        logger.debug("Closing connection")
        client_socket.close()

if __name__ == "__main__":
    run_client()
