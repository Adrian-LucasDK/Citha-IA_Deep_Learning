def ler_raio_valido():
    while True:
        try:
            raio = float(input("Digite o raio da pizza (em cm): "))
            if raio <= 0:
                print("Por favor, digite um raio maior que zero.")
            else:
                return raio
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def calcular_area_pizza(raio):
    pi = 3.14
    area = pi * (raio ** 2)
    return area

# Programa principal
raio = ler_raio_valido()
area = calcular_area_pizza(raio)

print(f"\nA área da pizza é: {area:.2f} cm²")
