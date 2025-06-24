# Programa para calcular a média ponderada de três notas com pesos 1, 2 e 3

# Função para ler e validar uma nota (0 a 10)
def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"digite a nota {numero} (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("nota inválida! deve estar entre 0 e 10.")
        except ValueError:
            print("por favor, digite um número válido.")

# Lê as três notas
nota1 = ler_nota(1)
nota2 = ler_nota(2)
nota3 = ler_nota(3)

# Define os pesos das notas
peso1 = 1
peso2 = 2
peso3 = 3

# Calcula a média ponderada
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Exibe a média ponderada formatada com 2 casas decimais
print(f"\na média ponderada do aluno é: {media:.2f}")
