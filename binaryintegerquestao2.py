def decimal_para_complemento2(n):
    if n < -128 or n > 127:
        raise ValueError("Número fora do intervalo de 8 bits em complemento a 2")
    if n < 0:
        return format((n + 256) & 255, "08b")
    else:
        return format(n & 255, "08b")


def complemento2_para_decimal(binario):
    if len(binario) != 8:
        raise ValueError("O binário deve ter exatamente 8 bits")
    valor = int(binario, 2)
    if valor > 127:
        return valor - 256
    return valor


def adicao_binaria(a, b):
    soma = bin(int(a, 2) + int(b, 2))[2:].zfill(8)
    return soma[-8:]  # Mantém apenas os 8 bits menos significativos


def verificar_overflow(a, b, resultado):
    a_sinal = int(a[0])
    b_sinal = int(b[0])
    r_sinal = int(resultado[0])
    return (a_sinal == b_sinal) and (a_sinal != r_sinal)


def operacao_complemento2(a, b, operacao):
    bin_a = decimal_para_complemento2(a)
    bin_b = decimal_para_complemento2(b)

    if operacao == "+":
        resultado_bin = adicao_binaria(bin_a, bin_b)
    elif operacao == "-":
        bin_b_negativo = decimal_para_complemento2(-b)
        resultado_bin = adicao_binaria(bin_a, bin_b_negativo)
    else:
        raise ValueError("Operação não suportada")

    overflow = verificar_overflow(bin_a, bin_b, resultado_bin)
    resultado_dec = complemento2_para_decimal(resultado_bin)

    return {
        "a_bin": bin_a,
        "b_bin": bin_b,
        "resultado_bin": resultado_bin,
        "resultado_dec": resultado_dec,
        "overflow": overflow,
    }


print("digite o valor da primeira operação e segunda")
a = input()
b = input()
resultado = operacao_complemento2(a, b, "+")
print(f"{a} + {b} = {resultado['resultado_dec']} ({resultado['resultado_bin']})")
print(f"Overflow: {resultado['overflow']}")

print("digite o valor da operação de a e b")
a = input()
b = input()
resultado = operacao_complemento2(a, b, "+")
print(f"{a} + {b} = {resultado['resultado_dec']} ({resultado['resultado_bin']})")
print(f"Overflow: {resultado['overflow']}")
