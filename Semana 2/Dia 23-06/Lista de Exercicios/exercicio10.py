import math  # Importa a biblioteca para funções matemáticas

# Função para ler um número float com validação
def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, digite um número válido.")

# Solicita as coordenadas do primeiro ponto
x1 = ler_float("Digite a coordenada x do primeiro ponto: ")
y1 = ler_float("Digite a coordenada y do primeiro ponto: ")

# Solicita as coordenadas do segundo ponto
x2 = ler_float("Digite a coordenada x do segundo ponto: ")
y2 = ler_float("Digite a coordenada y do segundo ponto: ")

# Calcula a distância entre os dois pontos usando a fórmula da distância euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Exibe o resultado formatado com 2 casas decimais
print(f"\nA distância entre os pontos é: {distancia:.2f}")
