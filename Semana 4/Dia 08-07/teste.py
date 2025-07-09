import numpy as np  # Importando numpy para manipulação de arrays
import pandas as pd  # Importando pandas para manipulação de DataFrames
import matplotlib.pyplot as plt  # Importando matplotlib para visualização de dados
# Importando função para dividir dados em treino e teste
from sklearn.model_selection import train_test_split
# Importando regressor de rede neural multi-layer perceptron
from sklearn.neural_network import MLPRegressor
# Importando função para normalização dos dados entre 0 e 1
from sklearn.preprocessing import MinMaxScaler
# Importando métricas de avaliação do modelo
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)  # Definindo semente para reprodutibilidade

dias = 1000  # Definindo o número de dias simulados

# Gerando dados de chuva com média de 10mm e desvio padrão de 3mm
chuvas = np.random.normal(10, 3, dias)

# Gerando dados de temperatura com média de 27°C e desvio padrão de 2°C
temperaturas = np.random.normal(27, 2, dias)

niveis_anteriores = np.cumsum(np.random.normal(
    0.1, 0.05, dias))  # Gerando dados de níveis do rio

nivel_real = niveis_anteriores + 0.05 * chuvas - 0.02 * temperaturas + \
    np.random.normal(
        0, 0.3, dias)  # Calculando o nível real do rio com base nos dados simulados

df = pd.DataFrame(
    {
        'chuvas': chuvas,
        'temperaturas': temperaturas,
        'niveis_anteriores': niveis_anteriores,
        'nivel_real': nivel_real
    }
)

# Variáveis independentes
X = df[['chuvas', 'temperaturas', 'niveis_anteriores']]
Y = df['nivel_real']  # Variável dependente

# Inicializando o normalizador para as variáveis independentes
scaler_X = MinMaxScaler()
scaler_Y = MinMaxScaler()  # Inicializando o normalizador para a variável dependente

X_scaled = scaler_X.fit_transform(X)  # Normalizando as variáveis independentes
# Normalizando a variável dependente
Y_scaled = scaler_Y.fit_transform(Y.values.reshape(-1, 1)).ravel()

x_train, x_test, y_train, y_test = train_test_split(
    X_scaled, Y_scaled, test_size=0.2, random_state=42)  # Dividindo os dados em treino e teste

mlp = MLPRegressor(hidden_layer_sizes=(10, 10), activation='relu', solver='adam',
                   max_iter=1000, random_state=42)  # Inicializando o modelo de rede neural

mlp.fit(x_train, y_train)  # Treinando o modelo

y_pred_scaled = mlp.predict(x_test)  # Fazendo previsões com o modelo

y_pred = scaler_Y.inverse_transform(
    y_pred_scaled.reshape(-1, 1)).ravel()  # Desnormalizando as previsões
y_test_original = scaler_Y.inverse_transform(
    y_test.reshape(-1, 1)).ravel()  # Desnormalizando os valores reais

# Calculando o erro quadrático médio (MSE)
print("MSE: ", mean_squared_error(y_test_original, y_pred))

# Calculando o coeficiente de determinação R²
print("R²: ", r2_score(y_test_original, y_pred))

plt.figure(figsize=(10, 5))  # Definindo o tamanho da figura
plt.plot(y_test_original[:50], label='nível_real', marker="o", color='blue')  # Plotando os valores reais
plt.plot(y_pred[:50], label='Previsto', marker="x", color='red')  # Plotando as previsões
plt.title('Nível do Rio: Real vs Previsto')  # Título do gráfico
plt.xlabel('Amostras')  # Rótulo do eixo x
plt.ylabel('Nível do Rio (m)')  # Rótulo do eixo y
plt.legend()  # Adicionando legenda
plt.grid(True)  # Adicionando grade ao gráfico
plt.tight_layout()  # Ajustando o layout do gráfico
plt.show()  # Exibindo o gráfico

