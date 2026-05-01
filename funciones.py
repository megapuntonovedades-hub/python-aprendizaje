"""Funciones reutilizables para saludos y comprobar mayoría de edad."""


def is_adult(age):
    return age >= 18


def greeting_line(name, age):
    return f"Hola, {name}. Tienes {age} años."


def adult_status_message(name, age):
    if is_adult(age):
        return f"{name}, eres mayor de edad."
    return f"{name}, aún eres menor de edad."
