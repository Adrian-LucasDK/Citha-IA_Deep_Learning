def ler_valor_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Por favor, digite um valor maior ou igual a zero.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
salario_fixo = ler_valor_positivo("Digite o salário fixo do funcionário: R$ ")
vendas = ler_valor_positivo("Digite o valor total das vendas: R$ ")

comissao = vendas * 0.04
salario_final = salario_fixo + comissao

print(f"\nComissão: R$ {comissao:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")
