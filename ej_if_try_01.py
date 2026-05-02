try:
    nota=int(input("ingrese el valor de la nota"))

except ValueError:
    print("solo se aceptan numeros")
else:
    if nota<0 or nota>100:
        print("Nota invalida")
    elif nota>=90:
        print("A")
    elif nota>=80 and nota<90:
        print("B")
    elif nota>=70 and nota<80:
        print("C")
    elif nota>=60 and nota<70:
        print("D")
    else:
        print("F")