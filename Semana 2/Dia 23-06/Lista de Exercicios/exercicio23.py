def ler_valor_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Digite um valor maior que zero.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
altura_pessoa = ler_valor_positivo("Digite a sua altura (em metros): ")
sombra_pessoa = ler_valor_positivo("Digite o comprimento da sua sombra (em metros): ")
sombra_predio = ler_valor_positivo("Digite o comprimento da sombra do prédio (em metros): ")

altura_predio = (altura_pessoa * sombra_predio) / sombra_pessoa

print(f"\nA altura do prédio é aproximadamente {altura_predio:.2f} metros.")
