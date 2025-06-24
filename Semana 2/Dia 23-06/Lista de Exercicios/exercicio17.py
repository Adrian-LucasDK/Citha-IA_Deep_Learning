def ler_temperatura_celsius():
    while True:
        try:
            celsius = float(input("Digite a temperatura em Celsius: "))
            return celsius
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def converter_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Programa principal
temp_celsius = ler_temperatura_celsius()
temp_fahrenheit = converter_para_fahrenheit(temp_celsius)

print(f"\n{temp_celsius:.2f}°C equivalem a {temp_fahrenheit:.2f}°F")
