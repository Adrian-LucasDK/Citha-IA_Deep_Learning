# Programa para calcular a arrecadação da padaria Hotpão e o valor a ser guardado na poupança

# Define os preços dos produtos
pao = 0.12   # Preço de cada pão francês em reais
broa = 1.50  # Preço de cada broa em reais

# Lê e valida a quantidade de pães vendidos
while True:
    try:
        paes = int(input("Digite a quantidade de pães vendidos no dia: "))
        if paes >= 0:
            break
        else:
            print("A quantidade de pães não pode ser negativa.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Lê e valida a quantidade de broas vendidas
while True:
    try:
        broas = int(input("Digite a quantidade de broas vendidas no dia: "))
        if broas >= 0:
            break
        else:
            print("A quantidade de broas não pode ser negativa.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Calcula o total arrecadado com os pães e broas
total_paes = paes * pao
total_broas = broas * broa
total = total_paes + total_broas

# Calcula 10% do total para guardar na poupança
poupanca = total * 0.10

# Exibe os resultados
print("\nRelatório de Vendas:")
print("Total arrecadado com pães: R$ {:.2f}".format(total_paes))
print("Total arrecadado com broas: R$ {:.2f}".format(total_broas))
print("Total geral arrecadado: R$ {:.2f}".format(total))
print("Valor a ser guardado na poupança (10%): R$ {:.2f}".format(poupanca))
