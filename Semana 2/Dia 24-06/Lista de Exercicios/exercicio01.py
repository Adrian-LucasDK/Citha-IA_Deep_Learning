# Solicita ao usuário que digite o valor de A e converte para número float
A = float(input("Digite o valor de A: "))

# Solicita ao usuário que digite o valor de B e converte para número float
B = float(input("Digite o valor de B: "))

# Solicita ao usuário que digite o valor de C e converte para número float
C = float(input("Digite o valor de C: "))

# Calcula a soma de A + B
soma = A + B

# Verifica se a soma de A + B é menor que C
if soma < C:
    print("A soma de A + B é menor que C.")
else:
    print("A soma de A + B NÃO é menor que C.")
