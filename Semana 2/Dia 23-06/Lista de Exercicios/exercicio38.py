def ler_ano(mensagem):
    while True:
        try:
            ano = int(input(mensagem))
            if ano <= 0:
                print("Digite um ano válido maior que zero.")
            else:
                return ano
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Programa principal
ano_nascimento = ler_ano("Digite o ano de nascimento: ")
ano_atual = ler_ano("Digite o ano atual: ")

if ano_atual < ano_nascimento:
    print("\nAno atual não pode ser menor que o ano de nascimento.")
else:
    idade_anos = ano_atual - ano_nascimento
    idade_meses = idade_anos * 12
    idade_dias = idade_anos * 365
    idade_semanas = idade_dias / 7

    print(f"\nIdade em anos: {idade_anos}")
    print(f"Idade em meses: {idade_meses}")
    print(f"Idade em dias: {idade_dias}")
    print(f"Idade em semanas: {idade_semanas:.0f}")
