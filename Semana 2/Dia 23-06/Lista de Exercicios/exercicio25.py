import math

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
raio = ler_valor_positivo("Digite o raio da base da caixa d'água (em metros): ")
altura = ler_valor_positivo("Digite a altura da caixa d'água (em metros): ")

volume = math.pi * (raio ** 2) * altura

print(f"\nO volume da caixa d'água é de aproximadamente {volume:.2f} metros cúbicos.")
