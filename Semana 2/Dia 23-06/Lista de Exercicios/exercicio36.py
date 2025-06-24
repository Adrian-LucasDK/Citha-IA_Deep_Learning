def ler_valor_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Digite um valor maior que zero.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
salario_minimo = ler_valor_positivo("Digite o valor do salário mínimo: R$ ")
salario_funcionario = ler_valor_positivo("Digite o salário do funcionário: R$ ")

quantidade = salario_funcionario / salario_minimo

print(f"\nO funcionário ganha {quantidade:.2f} salários mínimos.")
