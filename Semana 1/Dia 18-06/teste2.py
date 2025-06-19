# Simulador de saques em uma conta bancária
saldo = 1000.0  # Saldo inicial da conta

while saldo > 0:
    saque = float(input(f"Saldo atual: R$ {saldo:.2f}. Digite o valor do saque (ou 0 para sair): "))
    
    if saque == 0:
        print("Operação encerrada.")
        break
    
    if saque < 0:
        print("Valor de saque inválido. Tente novamente.")
        continue
    
    if saque > saldo:
        print("Saldo insuficiente para realizar o saque. Tente um valor menor.")
        continue
    
    saldo -= saque
    print(f"Saque de R$ {saque:.2f} realizado com sucesso. Saldo restante: R$ {saldo:.2f}.")