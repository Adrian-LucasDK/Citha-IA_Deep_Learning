def ler_quantidade_frangos():
    while True:
        try:
            quantidade = int(input("Digite a quantidade total de frangos na granja: "))
            if quantidade <= 0:
                print("Por favor, digite um número maior que zero.")
            else:
                return quantidade
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def calcular_custos(quantidade):
    custo_anel_chip = 4.00
    custo_anel_alimento = 3.50

    total_chip = quantidade * custo_anel_chip
    total_alimento = quantidade * 2 * custo_anel_alimento  # 2 anéis por frango
    gasto_total = total_chip + total_alimento

    return total_chip, total_alimento, gasto_total

# Programa principal
qtd_frangos = ler_quantidade_frangos()
total_chip, total_alimento, gasto = calcular_custos(qtd_frangos)

print(f"\nGasto com anéis de chip: R$ {total_chip:.2f}")
print(f"Gasto com anéis de alimento: R$ {total_alimento:.2f}")
print(f"Gasto total da granja: R$ {gasto:.2f}")
