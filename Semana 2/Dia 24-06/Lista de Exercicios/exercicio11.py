# Solicita o preço normal do produto
preco = float(input("Digite o preço do produto: R$ "))

# Mostra as opções de pagamento atualizadas
print("Condições de pagamento:")
print("1 - À vista em dinheiro ou cheque (10% de desconto)")
print("2 - À vista no cartão de crédito (15% de desconto)")
print("3 - Em duas vezes, preço normal sem juros")
print("4 - Em quatro vezes, preço normal mais 10% de juros")

# Solicita o código da condição de pagamento
codigo = int(input("Digite o código da condição de pagamento (1 a 4): "))

# Inicializa a variável para o valor final a pagar
valor_final = 0

# Verifica qual condição foi escolhida e calcula o valor final
if codigo == 1:
    # 10% de desconto no preço
    valor_final = preco * 0.90
elif codigo == 2:
    # 15% de desconto no preço
    valor_final = preco * 0.85
elif codigo == 3:
    # preço normal, sem juros em 2 vezes
    valor_final = preco
elif codigo == 4:
    # preço normal + 10% de juros em 4 vezes
    valor_final = preco * 1.10
else:
    # Caso o código seja inválido
    print("Código de pagamento inválido!")

# Se o código for válido, exibe o valor final e o valor de cada parcela se for parcelado
if codigo in [1, 2, 3, 4]:
    print(f"Valor total a pagar: R$ {valor_final:.2f}")
    if codigo == 3:
        print(f"Pagamento em 2 vezes de R$ {valor_final / 2:.2f} sem juros.")
    elif codigo == 4:
        print(f"Pagamento em 4 vezes de R$ {valor_final / 4:.2f} com juros.")
