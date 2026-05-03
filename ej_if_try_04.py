USUARIO_OK="admin"
CLAVE_OK="1234"

usuario=input("ingresa el usuario: ")
try:
    clave=int(input("ingrese clave"))
except ValueError:
    print("escriba solo numeros en la clave")
else:
    if usuario!=USUARIO_OK :
        print("Usuario incorrecto")
    elif clave!=int(CLAVE_OK):
        print("clave incorrecta")
    elif usuario==USUARIO_OK and clave!=int(CLAVE_OK):
        print("clave incorrecta")
    elif usuario!=USUARIO_OK and clave==int(CLAVE_OK):
        print("Usuario incorrecto")
    elif usuario!=USUARIO_OK and clave!=int(CLAVE_OK):
        print("Usuario incorrecto y clave incorrecta")
    else:
        print("Acceso permitido")
   
    
        