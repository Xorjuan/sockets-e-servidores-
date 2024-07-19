import socket
import logging

# Configuração do logger
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


def setup_client():
    host = "25.0.111.214"
    port = 65432
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s


def run_client():
    try:
        client_socket = setup_client()
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
