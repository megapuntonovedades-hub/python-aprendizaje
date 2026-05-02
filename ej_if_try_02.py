try:
    cantidad=int(input("ingrese cantidad de productos"))
    precio=float(input("ingrese precio del producto"))
except ValueError:
    print("solo ingrese numeros por favor")
else:
    if cantidad<0 or precio<0:
        print("Datos invalidos")
    else:
        subtotal=precio*cantidad
        if subtotal>=200:
            descuento=0.15
            total=subtotal-subtotal*descuento            
        elif subtotal>=100 and subtotal<200:
            descuento=0.1
            total=subtotal-subtotal*descuento
        else:
            descuento=0
            total=subtotal
        print(
            f"la cantidad es: {cantidad}",
            f"el precio es: {precio}",
            f"el subtotal es: {subtotal}",
            f"el descuento es: {descuento*100}%",
            f"el total a pagar es: {total:.2f}",
            sep="\n",
            )