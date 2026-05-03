try:
    peso=float(input("ingresa peso"))
    altura=float(input("ingresa altura"))
except ValueError:
    print("ingrese solo numeros por favor")
else:
    if peso<=0 or altura <=0:
        print("datos invalidos")
    else:
        imc=peso/(altura**2)
        if imc<18.5:
            print("bajo peso")
        elif imc>=18.5 and imc<25:
            print("normal")
        elif imc>=25 and imc<30:
            print("sobrepeso")
        else:
            print("obesidad")