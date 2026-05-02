try:
    nota = int(input("Ingrese el valor de la nota: "))
except ValueError:
    print("Solo se aceptan números enteros.")
else:
    if nota < 0 or nota > 100:
        print("Nota inválida")
    elif nota >= 90:
        print("A")
    elif nota >= 80:
        print("B")
    elif nota >= 70:
        print("C")
    elif nota >= 60:
        print("D")
    else:
        print("F")