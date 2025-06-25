# Solicita ao usuário que digite um número (pode ser decimal ou inteiro)
numero = float(input("Digite um número: "))

# Verifica se o número é positivo (maior ou igual a zero)
if numero >= 0:
    # Se for positivo, calcula o dobro
    resultado = numero * 2
else:
    # Se for negativo, calcula o triplo
    resultado = numero * 3

# Exibe o resultado na tela
print("O resultado é:", resultado)
