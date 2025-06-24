# Programa para venda de camisetas com interação por tamanho e quantidade
# Permite ao usuário continuar adicionando vendas até escolher sair

# Preços por tamanho
precos = {
    'p': 10.00,  # pequeno
    'm': 12.00,  # médio
    'g': 15.00   # grande
}

total = 0.0  # acumulador do valor total arrecadado

print("Venda de camisetas - digite 's' para sair.")

while True:
    # Solicita o tamanho da camiseta
    tamanho = input("Digite o tamanho da camiseta (p - pequeno, m - médio, g - grande) ou 's' para sair: ").lower()
    
    if tamanho == 's':
        # Sai do loop se o usuário quiser encerrar as vendas
        break
    
    if tamanho not in precos:
        print("Tamanho inválido! Por favor, digite p, m, g ou s.")
        continue  # volta para o início do loop
    
    # Solicita a quantidade da camiseta do tamanho escolhido
    while True:
        try:
            quantidade = int(input(f"Digite a quantidade de camisetas tamanho {tamanho}: "))
            if quantidade >= 0:
                break
            else:
                print("Quantidade deve ser zero ou maior.")
        except ValueError:
            print("Digite um número inteiro válido para a quantidade.")
    
    # Calcula o valor parcial da venda
    valor_venda = precos[tamanho] * quantidade
    
    # Acumula no total
    total += valor_venda
    
    print(f"Você adicionou {quantidade} camiseta(s) tamanho {tamanho} - valor parcial: R$ {valor_venda:.2f}")

# Exibe o valor total arrecadado após sair do loop
print(f"\nValor total arrecadado na venda: R$ {total:.2f}")
