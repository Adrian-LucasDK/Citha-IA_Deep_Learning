def ler_litros_positivos():
    while True:
        try:
            litros = float(input("Digite a quantidade total de refresco (em litros): "))
            if litros <= 0:
                print("Por favor, digite um valor maior que zero.")
            else:
                return litros
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
total_refresco = ler_litros_positivos()

agua = (8 / 10) * total_refresco
suco = (2 / 10) * total_refresco

print(f"\nPara fazer {total_refresco:.2f} litros de refresco, serão necessários:")
print(f"- {agua:.2f} litros de água mineral")
print(f"- {suco:.2f} litros de suco de maracujá")
