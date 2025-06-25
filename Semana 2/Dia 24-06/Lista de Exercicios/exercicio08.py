# Solicita ao usuário que digite o primeiro número inteiro
A = int(input("Digite o primeiro número (A): "))

# Solicita o segundo número inteiro
B = int(input("Digite o segundo número (B): "))

# Solicita o terceiro número inteiro
C = int(input("Digite o terceiro número (C): "))

# Verifica se todos os números são diferentes
if A != B and B != C and A != C:
    # Coloca os números em uma lista
    lista = [A, B, C]

    # Ordena a lista em ordem decrescente (do maior para o menor)
    lista.sort(reverse=True)

    # Exibe os números ordenados
    print("Números em ordem decrescente:", lista[0], lista[1], lista[2])
else:
    # Caso os números não sejam diferentes, exibe uma mensagem de erro
    print("Erro: os três números devem ser diferentes entre si.")
