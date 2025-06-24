def ler_quantidade_sanduiches():
    while True:
        try:
            quantidade = int(input("Digite a quantidade de sanduíches a preparar: "))
            if quantidade <= 0:
                print("Por favor, digite um número maior que zero.")
            else:
                return quantidade
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def calcular_ingredientes_em_kg(qtd_sanduiches):
    # Pesos em gramas por unidade
    queijo_por_sanduiche = 2 * 50   # 100g
    presunto_por_sanduiche = 50     # 50g
    carne_por_sanduiche = 100       # 100g

    # Total em gramas
    total_queijo = queijo_por_sanduiche * qtd_sanduiches
    total_presunto = presunto_por_sanduiche * qtd_sanduiches
    total_carne = carne_por_sanduiche * qtd_sanduiches

    # Convertendo para quilos (1kg = 1000g)
    return (
        total_queijo / 1000,
        total_presunto / 1000,
        total_carne / 1000
    )

# Programa principal
quantidade = ler_quantidade_sanduiches()
queijo_kg, presunto_kg, carne_kg = calcular_ingredientes_em_kg(quantidade)

print(f"\nPara {quantidade} sanduíche(s), será necessário:")
print(f"- {queijo_kg:.2f} kg de queijo")
print(f"- {presunto_kg:.2f} kg de presunto")
print(f"- {carne_kg:.2f} kg de carne (hambúrguer)")
