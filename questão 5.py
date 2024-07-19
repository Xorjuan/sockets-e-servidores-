import sys

# Matriz ASCII da imagem anterior
ascii_matrix = [
    ["NUL", "SOH", "STX", "ETX", "EOT", "ENO", "ACK", "BEL", "BS", "TAB", "LF", "VT", "FF", "CR", "SO", "SI"],
    ["DLE", "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB", "CAN", "EM", "SUB", "ESC", "FS", "GS", "RS", "US"],
    [" ", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/"],
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?"],
    ["@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_"],
    ["`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
    ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "DEL"]
]

# Tabela UTF-8 fornecida
utf8_table = [
    {"bytes": 1, "bits": 7, "first": "U+0000", "last": "U+007F"},
    {"bytes": 2, "bits": 11, "first": "U+0080", "last": "U+07FF"},
    {"bytes": 3, "bits": 16, "first": "U+0800", "last": "U+FFFF"},
    {"bytes": 4, "bits": 21, "first": "U+10000", "last": "U+10FFFF"}
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
        word = input("Digite uma palavra (ou 'voltar' para retornar ao menu principal): ")
        if word.lower() == 'voltar':
            break
        hex_result = word_to_hex(word)
        print(f"Valor hexadecimal de '{word}': {hex_result}")

def print_utf8_table():
    print("\nTabela UTF-8:")
    print("| Number of bytes | Bits for code point | First code point | Last code point |")
    print("|-----------------|---------------------|------------------|-----------------|")
    for row in utf8_table:
        print(f"| {row['bytes']:15d} | {row['bits']:19d} | {row['first']:16s} | {row['last']:14s} |")
    print()

def compare_utf8_bytes():
    print_utf8_table()

    phrase1 = input("Digite uma palavra sem acentos: ")
    phrase2 = input("Digite a mesma palavra com acentos: ")

    bytes1 = phrase1.encode('utf-8')
    bytes2 = phrase2.encode('utf-8')

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

        if choice == '1':
            ascii_to_hex()
        elif choice == '2':
            compare_utf8_bytes()
        elif choice == '3':
            print("Encerrando o programa...")
            sys.exit(0)
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main_menu()