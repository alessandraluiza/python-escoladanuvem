'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

temperatura = float(input("Digite o valor da temperatura: "))
origem = input("Informe a unidade de origem (C/F/K): ").upper()
destino = input("Informe a unidade de destino (C/F/K): ").upper()

# Conversão
resultado = None

# Celsius para outras unidades
if origem == "C":
    if destino == "F":
        resultado = (temperatura * 9/5) + 32
    elif destino == "K":
        resultado = temperatura + 273.15
    else:
        resultado = temperatura

# Fahrenheit para outras unidades
elif origem == "F":
    if destino == "C":
        resultado = (temperatura - 32) * 5/9
    elif destino == "K":
        resultado = (temperatura - 32) * 5/9 + 273.15
    else:
        resultado = temperatura

# Kelvin para outras unidades
elif origem == "K":
    if destino == "C":
        resultado = temperatura - 273.15
    elif destino == "F":
        resultado = (temperatura - 273.15) * 9/5 + 32
    else:
        resultado = temperatura
else:
    print("Unidade de origem inválida.")

# Exibição do resultado
if resultado is not None:
    print(f"\n{temperatura:.2f}°{origem} equivalem a {resultado:.2f}°{destino}")