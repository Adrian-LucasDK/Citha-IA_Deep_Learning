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
base_maior = ler_valor_positivo("Digite o valor da base maior do trapézio: ")
base_menor = ler_valor_positivo("Digite o valor da base menor do trapézio: ")
altura = ler_valor_positivo("Digite a altura do trapézio: ")

area = ((base_maior + base_menor) * altura) / 2

print(f"\nA área do trapézio é: {area:.2f}")
