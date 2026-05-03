try:
    peso = float(input("Ingrese el peso (kg): "))
    altura = float(input("Ingrese la altura (m): "))
except ValueError:
    print("Ingrese solo números.")
else:
    if peso <= 0 or altura <= 0:
        print("Datos inválidos")
    else:
        imc = peso / (altura ** 2)

        if imc < 18.5:
            print("Bajo peso")
        elif imc < 25:
            print("Normal")
        elif imc < 30:
            print("Sobrepeso")
        else:
            print("Obesidad")

        print(f"IMC: {imc:.2f}")