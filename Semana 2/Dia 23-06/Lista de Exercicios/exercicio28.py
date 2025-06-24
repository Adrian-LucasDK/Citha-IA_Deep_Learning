def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
nota1 = ler_nota("Digite a primeira nota (peso 2): ")
nota2 = ler_nota("Digite a segunda nota (peso 3): ")

media_ponderada = (nota1 * 2 + nota2 * 3) / (2 + 3)

print(f"\nA média ponderada das notas é: {media_ponderada:.2f}")
