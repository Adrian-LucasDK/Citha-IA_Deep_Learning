def ler_numero(mensagem):
    while True:
        try:
            num = float(input(mensagem))
            return num
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
num1 = ler_numero("Digite o primeiro número: ")
num2 = ler_numero("Digite o segundo número: ")
num3 = ler_numero("Digite o terceiro número: ")

resultado = num1 * num2 * num3

print(f"\nA multiplicação dos três números é: {resultado}")
