# Solicita ao usuário que digite o valor de A (inteiro)
A = int(input("Digite o valor de A: "))

# Solicita ao usuário que digite o valor de B (inteiro)
B = int(input("Digite o valor de B: "))

# Verifica se os valores A e B são iguais
if A == B:
    # Se forem iguais, soma A + B e atribui a C
    C = A + B
else:
    # Se forem diferentes, multiplica A por B e atribui a C
    C = A * B

# Exibe o resultado armazenado na variável C
print("O resultado é:", C)
