# Solicita o peso da pessoa em kg (pode ser decimal)
peso = float(input("Digite o seu peso em kg: "))

# Solicita a altura da pessoa em metros (exemplo: 1.75)
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC (Índice de Massa Corporal)
imc = peso / (altura ** 2)

# Mostra o valor do IMC com 2 casas decimais
print(f"Seu IMC é: {imc:.2f}")

# Verifica em qual faixa o IMC se encaixa e exibe a condição
if imc < 18.5:
    print("Condição: Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Condição: Peso normal")
elif imc >= 25 and imc < 30:
    print("Condição: Acima do peso")
else:  # imc >= 30
    print("Condição: Obeso")
