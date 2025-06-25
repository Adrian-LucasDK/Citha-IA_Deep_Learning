# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é divisível por 2 (ou seja, se é par)
if numero % 2 == 0:
    print("O número é PAR.")
else:
    # Se não for par, então é ímpar
    print("O número é ÍMPAR.")
