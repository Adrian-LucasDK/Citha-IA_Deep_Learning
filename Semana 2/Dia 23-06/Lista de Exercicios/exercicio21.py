def ler_quantidade_positivo(mensagem):
    while True:
        try:
            qtd = int(input(mensagem))
            if qtd < 0:
                print("Digite um número zero ou positivo.")
            else:
                return qtd
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Programa principal
latas_350 = ler_quantidade_positivo("Quantidade de latas de 350 ml: ")
garrafas_600 = ler_quantidade_positivo("Quantidade de garrafas de 600 ml: ")
garrafas_2l = ler_quantidade_positivo("Quantidade de garrafas de 2 litros: ")

# Convertendo tudo para litros
total_litros = (latas_350 * 350 + garrafas_600 * 600) / 1000 + garrafas_2l * 2

print(f"\nO comerciante comprou um total de {total_litros:.2f} litros de refrigerante.")
