# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par (ou seja, se o resto da divisão por 2 é 0)
if numero % 2 == 0:
    # Se for par, soma 5
    resultado = numero + 5
else:
    # Se for ímpar, soma 8
    resultado = numero + 8

# Exibe o resultado final
print("O resultado da operação é:", resultado)
