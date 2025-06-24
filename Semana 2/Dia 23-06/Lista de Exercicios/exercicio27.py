def ler_numero(mensagem):
    while True:
        try:
            num = float(input(mensagem))
            return num
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
num1 = ler_numero("Digite o primeiro número: ")
num2 = ler_numero("Digite o segundo número (diferente de zero): ")

resultado = num1 / num2

print(f"\nO resultado da divisão é: {resultado}")
