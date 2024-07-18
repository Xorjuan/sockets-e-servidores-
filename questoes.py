import struct


# questão 1
def convert_hex(hex):
    print(int(hex, 16))  # converte de str para int em base 16


def convert_bin(binario):
    print(bin(binario))  # converte em int -> bin


convert_hex(str(input("digite um valor para a conversão em hexa:")))
convert_bin(int(input("digite um valor para a conversão em binario:")))

# questão 2


def binario_para_decimal(binario):
    if binario[0] == "1":  # Número negativo
        return -(256 - int(binario, 2))
    return int(binario, 2)


def decimal_para_binario(decimal):
    if decimal < 0:
        return format(256 + decimal, "08b")
    return format(decimal, "08b")


def operacao_binaria(bin1, bin2, operacao):
    # Converte binários para decimal
    dec1 = binario_para_decimal(bin1)
    dec2 = binario_para_decimal(bin2)

    # Realiza a operação
    if operacao == "+":
        resultado_dec = dec1 + dec2
    elif operacao == "-":
        resultado_dec = dec1 - dec2
    else:
        raise ValueError("Operação inválida. Use '+' para soma ou '-' para subtração.")

    # Trata overflow
    if resultado_dec > 127 or resultado_dec < -128:
        print("Aviso: Ocorreu overflow!")

    # Converte o resultado de volta para binário
    return decimal_para_binario(resultado_dec % 256)


# Teste do algoritmo
bin1 = input("Digite o primeiro número binário de 8 bits: ")
bin2 = input("Digite o segundo número binário de 8 bits: ")
operacao = input("Digite a operação desejada (+ para soma, - para subtração): ")

resultado = operacao_binaria(bin1, bin2, operacao)
print(f"Resultado da operação: {resultado}")
print(f"Valor decimal: {binario_para_decimal(resultado)}")


# questão 3
def binary_to_decimal(binary):
    if binary[0] == "1":  # Número negativo
        inverted = "".join("1" if bit == "0" else "0" for bit in binary)
        return -(int(inverted, 2) + 1)
    return int(binary, 2)


def decimal_to_binary(decimal):
    if decimal < 0:
        positive = bin(abs(decimal))[2:].zfill(8)
        inverted = "".join("1" if bit == "0" else "0" for bit in positive)
        return bin(int(inverted, 2) + 1)[2:].zfill(8)
    return bin(decimal)[2:].zfill(8)


# Números binários fornecidos

print("digite o dividendo da operação")
dividendo = input()
print("digite o divisor da operação ")
divisor = input()

# Converter para decimal
dec_dividendo = binary_to_decimal(dividendo)
dec_divisor = binary_to_decimal(divisor)

# Realizar a divisão
if dec_divisor != 0:
    quociente = dec_dividendo // dec_divisor
else:
    quociente = "Erro: Divisão por zero"

# Converter o resultado de volta para binário em complemento de 2


resultado_binario = (
    decimal_to_binary(quociente) if isinstance(quociente, int) else quociente
)
print(f"Dividendo: {dividendo} ({dec_dividendo})")
print(f"Divisor: {divisor} ({dec_divisor})")
print(
    f"Quociente: {resultado_binario} ({quociente if isinstance(quociente, int) else 'N/A'})"
)

# questoe 4


def float_to_ieee754(num):
    pacote = struct.pack(">f", num)

    variavel = struct.unpack(">I", pacote)[0]

    binario = format(variavel, "032b")

    sinal = binario[0]
    expoente = binario[1:9]
    mantissa = binario[9:]

    return f"sinal : {sinal}\expoente: {expoente}\mantissa: {mantissa}"


entrada = input()
print(float_to_ieee754(float(entrada)))

# questão 5
import sys

# Matriz ASCII da imagem anterior
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
    [" ", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/"],
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?"],
    ["@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_"],
    ["`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
    ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "DEL"],
]

# Tabela UTF-8 fornecida
utf8_table = [
    {"bytes": 1, "bits": 7, "first": "U+0000", "last": "U+007F"},
    {"bytes": 2, "bits": 11, "first": "U+0080", "last": "U+07FF"},
    {"bytes": 3, "bits": 16, "first": "U+0800", "last": "U+FFFF"},
    {"bytes": 4, "bits": 21, "first": "U+10000", "last": "U+10FFFF"},
]


def find_char_position(char):
    for i, row in enumerate(ascii_matrix):
        if char in row:
            return i, row.index(char)
    return None


def char_to_hex(char):
    position = find_char_position(char)
    if position:
        row, col = position
        hex_value = row * 16 + col
        return f"{hex_value:02X}"
    return None


def word_to_hex(word):
    hex_values = []
    for char in word:
        hex_value = char_to_hex(char)
        if hex_value:
            hex_values.append(hex_value)
        else:
            print(f"Caractere '{char}' não encontrado na tabela ASCII.")
    return " ".join(hex_values)


def ascii_to_hex():
    while True:
        word = input(
            "Digite uma palavra (ou 'voltar' para retornar ao menu principal): "
        )
        if word.lower() == "voltar":
            break
        hex_result = word_to_hex(word)
        print(f"Valor hexadecimal de '{word}': {hex_result}")


def print_utf8_table():
    print("\nTabela UTF-8:")
    print(
        "| Number of bytes | Bits for code point | First code point | Last code point |"
    )
    print(
        "|-----------------|---------------------|------------------|-----------------|"
    )
    for row in utf8_table:
        print(
            f"| {row['bytes']:15d} | {row['bits']:19d} | {row['first']:16s} | {row['last']:14s} |"
        )
    print()


def compare_utf8_bytes():
    print_utf8_table()

    phrase1 = input("Digite uma palavra sem acentos: ")
    phrase2 = input("Digite a mesma palavra com acentos: ")

    bytes1 = phrase1.encode("utf-8")
    bytes2 = phrase2.encode("utf-8")

    print(f"\nFrase 1: '{phrase1}'")
    print(f"Bytes ocupados: {len(bytes1)}")
    print(f"Representação hexadecimal: {bytes1.hex()}")

    print(f"\nFrase 2: '{phrase2}'")
    print(f"Bytes ocupados: {len(bytes2)}")
    print(f"Representação hexadecimal: {bytes2.hex()}")

    print(f"\nDiferença em bytes: {len(bytes2) - len(bytes1)}")


def main_menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Converter ASCII para Hexadecimal")
        print("2. Comparar bytes em UTF-8")
        print("3. Sair")

        choice = input("Digite o número da opção desejada: ")

        if choice == "1":
            ascii_to_hex()
        elif choice == "2":
            compare_utf8_bytes()
        elif choice == "3":
            print("Encerrando o programa...")
            sys.exit(0)
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main_menu()


# questão 6
