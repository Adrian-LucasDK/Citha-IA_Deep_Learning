# Programa para calcular o valor a pagar no restaurante Bem-Bão
# baseado no peso do prato montado pelo cliente (em quilos)

# Preço por quilo do restaurante
quilo = 12.00

# Solicita e valida o peso do prato em quilos
while True:
    try:
        prato = float(input("digite o peso do prato (em quilos): "))
        if prato > 0:
            break
        else:
            print("o peso do prato deve ser maior que zero.")
    except ValueError:
        print("por favor, digite um valor numérico válido.")

# Calcula o valor a pagar
valor = prato * quilo

# Exibe o valor a pagar, formatado com 2 casas decimais
print(f"\no valor a pagar é: R$ {valor:.2f}")
