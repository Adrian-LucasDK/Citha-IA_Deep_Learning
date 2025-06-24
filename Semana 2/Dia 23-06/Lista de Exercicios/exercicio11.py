def ler_dias_validos():
    while True:
        try:
            dias = int(input("Digite a quantidade de dias sem acidentes: "))
            if dias <= 0:
                print("Por favor, digite um número maior que zero.")
            else:
                return dias
        except ValueError:
            print("Entrada inválida. Digite um número inteiro positivo.")

def converter_tempo(dias_totais):
    anos = dias_totais // 360
    resto = dias_totais % 360
    meses = resto // 30
    dias = resto % 30
    return anos, meses, dias

# Programa principal
dias_sem_acidente = ler_dias_validos()
anos, meses, dias = converter_tempo(dias_sem_acidente)

print(f"\nTempo sem acidentes: {anos} ano(s), {meses} mês(es) e {dias} dia(s).")
