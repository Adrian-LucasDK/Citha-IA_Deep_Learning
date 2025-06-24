def ler_peso_kg():
    while True:
        try:
            peso_kg = float(input("Digite o peso da pessoa em quilos (kg): "))
            if peso_kg <= 0:
                print("Por favor, digite um peso maior que zero.")
            else:
                return peso_kg
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
peso_kg = ler_peso_kg()
peso_gramas = peso_kg * 1000

print(f"\nO peso da pessoa em gramas é: {peso_gramas:.2f} g")
