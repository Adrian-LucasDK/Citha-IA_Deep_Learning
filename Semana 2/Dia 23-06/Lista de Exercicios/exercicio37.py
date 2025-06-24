def ler_numero_inteiro(mensagem):
    while True:
        try:
            num = int(input(mensagem))
            return num
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Programa principal
numero = ler_numero_inteiro("Digite um número para ver a tabuada: ")

print(f"\nTabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
