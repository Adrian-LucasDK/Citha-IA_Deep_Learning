# Programa para calcular a área de um terreno retangular
# Desenvolvido para a imobiliária Imóbilis

# Solicita ao usuário que digite a largura do terreno
# Repete até que seja digitado um valor maior que zero
while True:
    try:
        largura = float(input("Digite a largura do terreno (em metros): "))
        if largura > 0:
            break  # Se o valor for válido, sai do loop
        else:
            print("A largura deve ser um número positivo maior que zero.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Solicita ao usuário que digite o comprimento do terreno
# Repete até que seja digitado um valor maior que zero
while True:
    try:
        comprimento = float(input("Digite o comprimento do terreno (em metros): "))
        if comprimento > 0:
            break  # Se o valor for válido, sai do loop
        else:
            print("O comprimento deve ser um número positivo maior que zero.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Calcula a área do terreno (largura × comprimento)
area = largura * comprimento

# Exibe o resultado da área do terreno
print("A área do terreno é:", area, "metros quadrados")
