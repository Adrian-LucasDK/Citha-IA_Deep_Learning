# Programa para calcular quantos dias se passaram desde o início do ano
# considerando que cada mês tem 30 dias

# Lê e valida o mês (1 a 12)
while True:
    try:
        mes = int(input("digite o mês (1 a 12): "))
        if 1 <= mes <= 12:
            break
        else:
            print("por favor, digite um mês entre 1 e 12.")
    except ValueError:
        print("por favor, digite um número inteiro válido para o mês.")

# Lê e valida o dia (1 a 30)
while True:
    try:
        dia = int(input("digite o dia (1 a 30): "))
        if 1 <= dia <= 30:
            break
        else:
            print("por favor, digite um dia entre 1 e 30.")
    except ValueError:
        print("por favor, digite um número inteiro válido para o dia.")

# Calcula os dias passados desde o início do ano
dias = (mes - 1) * 30 + dia

# Exibe o resultado
print(f"\njá se passaram {dias} dias desde o início do ano.")
