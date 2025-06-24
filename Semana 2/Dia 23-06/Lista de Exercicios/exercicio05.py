# Programa para calcular quantos litros de gasolina o motorista consegue colocar no tanque
# com base no valor do pagamento e no preço por litro

# Solicita e valida o preço do litro da gasolina
while True:
    try:
        litro = float(input("digite o preço do litro da gasolina (ex: 5.59): "))
        if litro > 0:
            break
        else:
            print("o preço do litro deve ser maior que zero.")
    except ValueError:
        print("por favor, digite um valor numérico válido.")

# Solicita e valida o valor que o motorista deseja colocar
while True:
    try:
        pagamento = float(input("digite o valor em reais que deseja colocar no tanque: "))
        if pagamento > 0:
            break
        else:
            print("o valor do pagamento deve ser maior que zero.")
    except ValueError:
        print("por favor, digite um valor numérico válido.")

# Calcula a quantidade de litros que será colocada no tanque
abastecido = pagamento / litro

# Exibe o resultado
print(f"\ncom R$ {pagamento:.2f}, você conseguirá colocar {abastecido:.2f} litros de gasolina no tanque.")
