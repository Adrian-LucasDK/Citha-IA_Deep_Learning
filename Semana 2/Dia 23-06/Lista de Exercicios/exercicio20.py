def ler_numero_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Por favor, digite um número maior que zero.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
blusas = ler_numero_positivo("Digite a quantidade de blusas produzidas: ")
novelos = ler_numero_positivo("Digite a quantidade total de novelos usados: ")

novelos_por_blusa = novelos / blusas

print(f"\nSão gastos {novelos_por_blusa:.2f} novelos de lã por blusa produzida.")
