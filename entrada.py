"""Práctica: entrada por consola, f-strings y condicional vía funciones."""

from funciones import adult_status_message, greeting_line

name = input("¿Cómo te llamas? ").strip()

age_text = input("¿Cuántos años tienes? ").strip()
age = int(age_text)

print(greeting_line(name, age))
print(adult_status_message(name, age))
