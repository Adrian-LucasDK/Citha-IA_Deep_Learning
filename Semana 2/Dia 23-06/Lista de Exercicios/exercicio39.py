salario = 1200.00
conta1 = 200.00
conta2 = 120.00
multa_percentual = 0.02  # 2%

# Calculando multas
multa_c1 = conta1 * multa_percentual
multa_c2 = conta2 * multa_percentual

# Total a pagar
total_c1 = conta1 + multa_c1
total_c2 = conta2 + multa_c2
total_pagar = total_c1 + total_c2

# Saldo restante
saldo_restante = salario - total_pagar

print(f"Salário inicial: R$ {salario:.2f}")
print(f"Conta 1 com multa: R$ {total_c1:.2f}")
print(f"Conta 2 com multa: R$ {total_c2:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")
print(f"Saldo restante do salário: R$ {saldo_restante:.2f}")
