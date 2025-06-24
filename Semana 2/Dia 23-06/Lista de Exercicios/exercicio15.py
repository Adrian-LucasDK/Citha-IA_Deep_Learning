def ler_valor_total():
    while True:
        try:
            total = float(input("Digite o valor total da conta: R$ "))
            if total <= 0:
                print("O valor deve ser maior que zero.")
            else:
                return total
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
total = ler_valor_total()

valor_por_pessoa = total / 3
valor_carlos = int(valor_por_pessoa)      # sem centavos
valor_andre = int(valor_por_pessoa)       # sem centavos
valor_felipe = total - valor_carlos - valor_andre  # paga o restante com centavos

# Exibindo resultados
print(f"\nCarlos deve pagar: R$ {valor_carlos:.2f}")
print(f"André deve pagar:  R$ {valor_andre:.2f}")
print(f"Felipe deve pagar: R$ {valor_felipe:.2f}")
