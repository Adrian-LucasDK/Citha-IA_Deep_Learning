from datetime import datetime, date

# Solicita o nome da pessoa
nome = input("digite o seu nome: ").strip()

# Solicita e valida a data de nascimento
while True:
    try:
        # Solicita dia, mês e ano separadamente
        dia = int(input("digite o dia do seu nascimento (1 a 31): "))
        mes = int(input("digite o mês do seu nascimento (1 a 12): "))
        ano = int(input("digite o ano do seu nascimento (ex: 2000): "))
        
        # Tenta criar uma data com os valores informados
        data_nascimento = date(ano, mes, dia)
        data_atual = date.today()

        # Verifica se a data é no futuro
        if data_nascimento > data_atual:
            print("a data de nascimento não pode ser no futuro.")
        else:
            break  # Data válida
    except ValueError:
        print("data inválida! verifique os valores e tente novamente.")

# Calcula a idade em anos completos
hoje = date.today()
idade_anos = hoje.year - data_nascimento.year

# Ajusta a idade se o aniversário ainda não chegou este ano
if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
    idade_anos -= 1

# Calcula a quantidade exata de dias vividos
dias_de_vida = (hoje - data_nascimento).days

# Exibe os resultados formatados em letras minúsculas
print(f"\n{nome.lower()}, você já viveu {dias_de_vida} dias.")
print(f"sua idade atual é de {idade_anos} anos completos.")
