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
cateto1 = ler_valor_positivo("Digite o valor do primeiro cateto: ")
cateto2 = ler_valor_positivo("Digite o valor do segundo cateto: ")

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"\nO valor da hipotenusa é: {hipotenusa:.2f}")
