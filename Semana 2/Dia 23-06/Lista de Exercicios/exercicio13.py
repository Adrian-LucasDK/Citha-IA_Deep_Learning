def ler_numero_valido():
    while True:
        try:
            numero = int(input("Digite um número inteiro de até 3 dígitos (0 a 999): "))
            if 0 <= numero <= 999:
                return numero
            else:
                print("Número fora do intervalo permitido. Digite de 0 a 999.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def separar_digitos(numero):
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10
    return centena, dezena, unidade

# Programa principal
numero = ler_numero_valido()
centena, dezena, unidade = separar_digitos(numero)

print(f"\nCENTENA = {centena}")
print(f"DEZENA  = {dezena}")
print(f"UNIDADE = {unidade}")
