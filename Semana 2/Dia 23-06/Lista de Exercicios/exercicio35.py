def ler_valor_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Digite um valor maior que zero.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
diagonal_maior = ler_valor_positivo("Digite o valor da diagonal maior do losango: ")
diagonal_menor = ler_valor_positivo("Digite o valor da diagonal menor do losango: ")

area = (diagonal_maior * diagonal_menor) / 2

print(f"\nA área do losango é: {area:.2f}")
