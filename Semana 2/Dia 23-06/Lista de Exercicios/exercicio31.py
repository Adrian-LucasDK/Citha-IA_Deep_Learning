def ler_peso():
    while True:
        try:
            peso = float(input("Digite o peso atual da pessoa (kg): "))
            if peso <= 0:
                print("Por favor, digite um peso maior que zero.")
            else:
                return peso
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
peso_atual = ler_peso()

peso_mais = peso_atual * 1.15  # engordar 15%
peso_menos = peso_atual * 0.80  # emagrecer 20%

print(f"\nNovo peso se engordar 15%: {peso_mais:.2f} kg")
print(f"Novo peso se emagrecer 20%: {peso_menos:.2f} kg")
