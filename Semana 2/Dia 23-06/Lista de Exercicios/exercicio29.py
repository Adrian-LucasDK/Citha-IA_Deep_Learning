def ler_preco(mensagem):
    while True:
        try:
            preco = float(input(mensagem))
            if preco < 0:
                print("O preço não pode ser negativo.")
            else:
                return preco
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
preco_original = ler_preco("Digite o preço do produto: R$ ")

novo_preco = preco_original * 0.90  # desconto de 10%

print(f"\nO novo preço com desconto é: R$ {novo_preco:.2f}")
