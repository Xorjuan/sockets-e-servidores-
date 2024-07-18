import socket
import struct
import sys


def convert_hex(hex_val):
    return str(int(hex_val, 16))


def convert_bin(binario):
    return bin(binario)


def questao1():
    hex_val = input("Digite um valor para a conversão em hexa: ")
    bin_val = int(input("Digite um valor para a conversão em binário: "))
    return convert_hex(hex_val), convert_bin(bin_val)


def binario_para_decimal(binario):
    if binario[0] == "1":
        return -(256 - int(binario, 2))
    return int(binario, 2)


def decimal_para_binario(decimal):
    if decimal < 0:
        return format(256 + decimal, "08b")
    return format(decimal, "08b")


def operacao_binaria(bin1, bin2, operacao):
    dec1 = binario_para_decimal(bin1)
    dec2 = binario_para_decimal(bin2)
    if operacao == "+":
        resultado_dec = dec1 + dec2
    elif operacao == "-":
        resultado_dec = dec1 - dec2
    else:
        raise ValueError("Operação inválida. Use '+' para soma ou '-' para subtração.")
    if resultado_dec > 127 or resultado_dec < -128:
        return "Aviso: Ocorreu overflow!"
    return decimal_para_binario(resultado_dec % 256)


def questao2():
    bin1 = input("Digite o primeiro número binário de 8 bits: ")
    bin2 = input("Digite o segundo número binário de 8 bits: ")
    operacao = input("Digite a operação desejada (+ para soma, - para subtração): ")
    resultado = operacao_binaria(bin1, bin2, operacao)
    return resultado, binario_para_decimal(resultado)


def binary_to_decimal(binary):
    if binary[0] == "1":
        inverted = "".join("1" if bit == "0" else "0" for bit in binary)
        return -(int(inverted, 2) + 1)
    return int(binary, 2)


def decimal_to_binary(decimal):
    if decimal < 0:
        positive = bin(abs(decimal))[2:].zfill(8)
        inverted = "".join("1" if bit == "0" else "0" for bit in positive)
        return bin(int(inverted, 2) + 1)[2:].zfill(8)
    return bin(decimal)[2:].zfill(8)


def questao3():
    dividendo = input("Digite o dividendo da operação: ")
    divisor = input("Digite o divisor da operação: ")
    dec_dividendo = binary_to_decimal(dividendo)
    dec_divisor = binary_to_decimal(divisor)
    if dec_divisor != 0:
        quociente = dec_dividendo // dec_divisor
    else:
        quociente = "Erro: Divisão por zero"
    resultado_binario = (
        decimal_to_binary(quociente) if isinstance(quociente, int) else quociente
    )
    return (
        dividendo,
        dec_dividendo,
        divisor,
        dec_divisor,
        resultado_binario,
        quociente,
    )


def float_to_ieee754(num):
    pacote = struct.pack(">f", num)
    variavel = struct.unpack(">I", pacote)[0]
    binario = format(variavel, "032b")
    sinal = binario[0]
    expoente = binario[1:9]
    mantissa = binario[9:]
    return f"sinal: {sinal}\nexpoente: {expoente}\nmantissa: {mantissa}"


def questao4():
    entrada = float(input("Digite um número para converter para IEEE 754: "))
    return float_to_ieee754(entrada)


def ascii_to_hex(word, ascii_matrix):
    hex_values = []
    for char in word:
        hex_value = char_to_hex(char, ascii_matrix)
        if hex_value:
            hex_values.append(hex_value)
        else:
            hex_values.append(f"Caractere '{char}' não encontrado na tabela ASCII.")
    return " ".join(hex_values)


def char_to_hex(char, ascii_matrix):
    for i, row in enumerate(ascii_matrix):
        if char in row:
            return f"{i * 16 + row.index(char):02X}"
    return None


def compare_utf8_bytes(phrase1, phrase2):
    bytes1 = phrase1.encode("utf-8")
    bytes2 = phrase2.encode("utf-8")
    return {
        "phrase1": phrase1,
        "bytes1": len(bytes1),
        "hex1": bytes1.hex(),
        "phrase2": phrase2,
        "bytes2": len(bytes2),
        "hex2": bytes2.hex(),
        "difference": len(bytes2) - len(bytes1),
    }


def questao5():
    ascii_matrix = [
        [
            "NUL",
            "SOH",
            "STX",
            "ETX",
            "EOT",
            "ENO",
            "ACK",
            "BEL",
            "BS",
            "TAB",
            "LF",
            "VT",
            "FF",
            "CR",
            "SO",
            "SI",
        ],
        [
            "DLE",
            "DC1",
            "DC2",
            "DC3",
            "DC4",
            "NAK",
            "SYN",
            "ETB",
            "CAN",
            "EM",
            "SUB",
            "ESC",
            "FS",
            "GS",
            "RS",
            "US",
        ],
        [
            " ",
            "!",
            '"',
            "#",
            "$",
            "%",
            "&",
            "'",
            "(",
            ")",
            "*",
            "+",
            ",",
            "-",
            ".",
            "/",
        ],
        [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            ":",
            ";",
            "<",
            "=",
            ">",
            "?",
        ],
        [
            "@",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
        ],
        [
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "[",
            "\\",
            "]",
            "^",
            "_",
        ],
        [
            "`",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
        ],
        [
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "{",
            "|",
            "}",
            "~",
            "DEL",
        ],
    ]
    utf8_table = [
        {"bytes": 1, "bits": 7, "first": "U+0000", "last": "U+007F"},
        {"bytes": 2, "bits": 11, "first": "U+0080", "last": "U+07FF"},
        {"bytes": 3, "bits": 16, "first": "U+0800", "last": "U+FFFF"},
        {"bytes": 4, "bits": 21, "first": "U+10000", "last": "U+10FFFF"},
    ]
    while True:
        print("\nEscolha uma opção:")
        print("1. Converter ASCII para Hexadecimal")
        print("2. Comparar bytes em UTF-8")
        print("3. Voltar ao menu principal")

        choice = input("Digite o número da opção desejada: ")

        if choice == "1":
            word = input("Digite uma palavra: ")
            return ascii_to_hex(word, ascii_matrix)
        elif choice == "2":
            phrase1 = input("Digite uma palavra sem acentos: ")
            phrase2 = input("Digite a mesma palavra com acentos: ")
            return compare_utf8_bytes(phrase1, phrase2)
        elif choice == "3":
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


def handle_client(connection):
    try:
        while True:
            data = connection.recv(1024).decode()
            if not data:
                break

            if data == "1":
                response = questao1()
            elif data == "2":
                response = questao2()
            elif data == "3":
                response = questao3()
            elif data == "4":
                response = questao4()
            elif data == "5":
                response = questao5()
            elif data == "6":
                connection.sendall("Encerrando conexão...".encode())
                break
            else:
                response = "Opção inválida. Por favor, tente novamente."

            connection.sendall(str(response).encode())
    finally:
        connection.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 65432)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("Servidor aguardando conexões...")

    while True:
        connection, client_address = server_socket.accept()
        handle_client(connection)


if __name__ == "__main__":
    start_server()
