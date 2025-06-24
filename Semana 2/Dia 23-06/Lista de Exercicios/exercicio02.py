# Programa para calcular quantas ferraduras são necessárias para equipar os cavalos de um haras

# Loop para garantir que o número de cavalos seja um valor válido (inteiro e positivo)
while True:
    try:
        # Solicita ao usuário o número de cavalos
        cavalos = int(input("Digite a quantidade de cavalos comprados para o haras: "))
        
        # Verifica se o valor é maior que zero
        if cavalos > 0:
            break  # Se for válido, sai do loop
        else:
            print("A quantidade de cavalos deve ser maior que zero.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Cada cavalo precisa de 4 ferraduras
ferraduras = cavalos * 4

# Exibe o resultado na tela
print("Serão necessárias", ferraduras, "ferraduras para equipar todos os cavalos.")
