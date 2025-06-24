# Programa para calcular quantos dias de vida uma pessoa já viveu
# Considerando apenas anos completos de 365 dias

# Solicita o nome da pessoa
nome = input("Digite o seu nome: ").strip().upper()  # Remove espaços e coloca em maiúsculas

# Solicita e valida a idade da pessoa
while True:
    try:
        idade = int(input("Digite a sua idade (em anos completos): "))
        if idade >= 0:
            break
        else:
            print("A idade não pode ser negativa.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Calcula a quantidade de dias vividos (sem considerar anos bissextos)
dias = idade * 365

# Exibe a mensagem com o nome e o total de dias vividos
print(f"\n{nome}, você já viveu {dias} dias.")
