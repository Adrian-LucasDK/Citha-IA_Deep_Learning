def ler_lado():
    while True:
        try:
            lado = float(input("Digite o valor do lado do quadrado: "))
            if lado <= 0:
                print("Por favor, digite um valor maior que zero.")
            else:
                return lado
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Programa principal
lado = ler_lado()
area = lado * lado

print(f"\nA área do quadrado é: {area:.2f}")
