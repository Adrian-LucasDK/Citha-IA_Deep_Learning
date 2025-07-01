import numpy as np  # Importa a biblioteca NumPy para operações com arrays e álgebra linear


# Define a classe Perceptron
class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        # Inicializa os pesos como zeros (um peso para cada entrada + 1 para o bias)
        self.weights = np.zeros(input_size + 1)
        # Define a taxa de aprendizado
        self.lr = learning_rate

    # Função de ativação: retorna 1 se a soma ponderada for >= 0, senão retorna 0
    def activation(self, x):
        return 1 if x >= 0 else 0

    # Método para prever a saída para uma dada entrada
    def predict(self, x):
        # Adiciona o bias (valor 1) no início do vetor de entrada
        x_with_bias = np.insert(x, 0, 1)
        # Calcula a soma ponderada dos pesos pelas entradas
        weighted_sum = np.dot(self.weights, x_with_bias)
        # Aplica a função de ativação e retorna o resultado
        return self.activation(weighted_sum)

    # Método de treinamento do perceptron
    def train(self, training_inputs, labels, epochs=10):
        # Repete o processo por um número de épocas
        for _ in range(epochs):
            # Para cada par entrada/saída esperada
            for x_val, label in zip(training_inputs, labels):
                # Calcula a previsão atual
                prediction = self.predict(x_val)
                # Calcula o erro (diferença entre esperado e previsto)
                error = label - prediction
                # Adiciona o bias à entrada
                x_with_bias = np.insert(x_val, 0, 1)
                # Atualiza os pesos com base no erro e na taxa de aprendizado
                self.weights += self.lr * error * x_with_bias


# Bloco principal: executado apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    # Define os dados de entrada (tabela verdade do AND)
    inputs = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    # Define as saídas esperadas (label) para a operação lógica AND
    labels = np.array([0, 0, 0, 1])

    # Cria um perceptron com 2 entradas
    perceptron = Perceptron(input_size=2)

    # Treina o perceptron com os dados fornecidos por 10 épocas
    perceptron.train(inputs, labels, epochs=10)

    # Mostra os pesos finais aprendidos
    print("Pesos finais:", perceptron.weights)

    # Testa o perceptron com as entradas e exibe a saída prevista
    print("Testes:")
    for x_val in inputs:
        print(f"Entrada: {x_val}, Saída: {perceptron.predict(x_val)}")
