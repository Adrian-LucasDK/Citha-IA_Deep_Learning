def ler_quantidade_moedas(tipo_moeda):
    while True:
        try:
            qtd = int(input(f"Digite a quantidade de moedas de {tipo_moeda}: "))
            if qtd < 0:
                print("Digite um número zero ou positivo.")
            else:
                return qtd
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Programa principal
moedas_1_cent = ler_quantidade_moedas("1 centavo")
moedas_5_cent = ler_quantidade_moedas("5 centavos")
moedas_10_cent = ler_quantidade_moedas("10 centavos")
moedas_25_cent = ler_quantidade_moedas("25 centavos")
moedas_50_cent = ler_quantidade_moedas("50 centavos")
moedas_1_real = ler_quantidade_moedas("1 real")

# Calculando o total em reais
total_reais = (
    moedas_1_cent * 0.01 +
    moedas_5_cent * 0.05 +
    moedas_10_cent * 0.10 +
    moedas_25_cent * 0.25 +
    moedas_50_cent * 0.50 +
    moedas_1_real * 1.00
)

print(f"\nTotal economizado: R$ {total_reais:.2f}")
