def es_adulto(edad: int) -> bool:
    return edad >= 18


def formatear_usuario(nombre: str, edad: int, correo: str) -> str:
    adulto = es_adulto(edad)
    return "\n".join(
        [
            f"Nombre: {nombre}",
            f"Edad: {edad}",
            f"Adulto: {adulto}",
            f"Correo: {correo}",
        ]
    )


def imprimir_usuario(nombre: str, edad: int, correo: str) -> None:
    print(formatear_usuario(nombre, edad, correo))


if __name__ == "__main__":
    name = "francisco"
    age = 33
    mail = "usuario@ejemplo.com"

    imprimir_usuario(name, age, mail)
