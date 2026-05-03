USUARIO_OK = "admin"
CLAVE_OK = 1234
usuario = input("Ingresa el usuario: ")
try:
    clave = int(input("Ingrese la clave: "))
except ValueError:
    print("La clave debe ser solo números")
else:
    if usuario != USUARIO_OK:
        print("Usuario incorrecto")
    elif clave != CLAVE_OK:
        print("Clave incorrecta")
    else:
        print("Acceso permitido")