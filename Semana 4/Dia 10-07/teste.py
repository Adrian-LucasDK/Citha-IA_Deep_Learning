import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore   
from tensorflow.keras.layers import SimpleRNN, Dense, Dropout # type: ignore
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# ================================
# 1. Simulação de dados realistas
# ================================
num_samples = 1000
sequence_length = 24
features = 3

# Simulação com distribuição normal
velocidade = np.random.normal(loc=1.0, scale=0.3, size=(num_samples, sequence_length, 1))
profundidade = np.random.normal(loc=10.0, scale=2.0, size=(num_samples, sequence_length, 1))
viradas = np.random.normal(loc=0.5, scale=0.2, size=(num_samples, sequence_length, 1))

# Juntando as 3 variáveis
X = np.concatenate([velocidade, profundidade, viradas], axis=2)

# ============================================
# 2. Geração de rótulos com base em percentis
# ============================================
frequencia_mudancas = X[:, :, 2].mean(axis=1)
variabilidade_velocidade = X[:, :, 0].std(axis=1)

limite_freq = np.percentile(frequencia_mudancas, 85)
limite_var = np.percentile(variabilidade_velocidade, 85)

labels = ((frequencia_mudancas > limite_freq) | (variabilidade_velocidade > limite_var)).astype(int)

# ========================================
# 3. Divisão dos dados em treino e teste
# ========================================
x_train, x_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# ================================
# 4. Construção da rede RNN
# ================================
model = Sequential()
model.add(SimpleRNN(64, input_shape=(sequence_length, features), activation='tanh'))
model.add(Dropout(0.3))  # Reduz overfitting
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# ================================
# 5. Treinamento com EarlyStopping
# ================================
from tensorflow.keras.callbacks import EarlyStopping # type: ignore

early_stop = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

history = model.fit(
    x_train, y_train,
    epochs=50,
    batch_size=16,
    validation_split=0.2,
    callbacks=[early_stop]
)

# ================================
# 6. Avaliação com métricas extras
# ================================
y_pred = (model.predict(x_test) > 0.5).astype(int)

print("\nRelatório de Classificação:\n")
print(classification_report(y_test, y_pred))

# ================================
# 7. Visualização dos resultados
# ================================
plt.figure(figsize=(12, 5))

# Acurácia
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Treinamento')
plt.plot(history.history['val_accuracy'], label='Validação')
plt.axvline(np.argmax(history.history['val_accuracy']), color='red', linestyle='--', label='Melhor Validação')
plt.title('Acurácia por Época')
plt.xlabel('Épocas')
plt.ylabel('Acurácia')
plt.grid(True)
plt.legend()

# Perda
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Treinamento')
plt.plot(history.history['val_loss'], label='Validação')
plt.axvline(np.argmin(history.history['val_loss']), color='red', linestyle='--', label='Menor Validação')
plt.title('Perda por Época')
plt.xlabel('Épocas')
plt.ylabel('Perda')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# ================================
# 8. Salvamento do modelo treinado
# ================================
model.save("modelo_peixes_rnn.h5")
print("Modelo salvo como 'modelo_peixes_rnn.h5'")
