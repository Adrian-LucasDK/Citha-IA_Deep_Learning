def ler_salario_valido():
    while True:
        try:
            salario = float(input("Digite o salário do funcionário: R$ "))
            if salario <= 0:
                print("Por favor, digite um salário maior que zero.")
            else:
                return salario
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def calcular_salario(salario_inicial):
    salario_com_aumento = salario_inicial * 1.15  # aumento de 15%
    salario_final = salario_com_aumento * 0.92    # desconto de 8%
    return salario_com_aumento, salario_final

# Programa principal
salario_inicial = ler_salario_valido()
salario_com_aumento, salario_final = calcular_salario(salario_inicial)

# Impressão formatada
print(f"\nSalário inicial:       R$ {salario_inicial:.2f}")
print(f"Salário com aumento:   R$ {salario_com_aumento:.2f}")
print(f"Salário final (líquido): R$ {salario_final:.2f}")
