def ler_horas_trabalhadas(tipo):
    while True:
        try:
            horas = float(input(f"Digite a quantidade de horas {tipo} trabalhadas: "))
            if horas < 0:
                print("A quantidade de horas não pode ser negativa.")
            else:
                return horas
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def calcular_salarios(horas_normais, horas_extras):
    salario_bruto = (horas_normais * 10) + (horas_extras * 15)
    salario_liquido = salario_bruto * 0.90  # descontando 10%
    return salario_bruto, salario_liquido

# Programa principal
horas_normais = ler_horas_trabalhadas("normais")
horas_extras = ler_horas_trabalhadas("extras")

bruto, liquido = calcular_salarios(horas_normais, horas_extras)

print(f"\nSalário bruto:  R$ {bruto:.2f}")
print(f"Salário líquido: R$ {liquido:.2f}")
