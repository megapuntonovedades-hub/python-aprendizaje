"""Ejercicios cortos: if/elif/else y bucles for."""


def nota_texto(score):
    if score >= 9:
        return "Sobresaliente"
    if score >= 7:
        return "Notable"
    if score >= 5:
        return "Aprobado"
    return "Suspendido"


def cuenta_atras(desde):
    print("Cuenta atrás:")
    for n in range(desde, 0, -1):
        print(f"  {n}")
    print("  ¡Ya!")


def saluda_clientes(names):
    print("Lista de clientes:")
    for name in names:
        print(f"  Hola, {name}")


if __name__ == "__main__":
    ejemplo_nota = 8
    print(f"Nota {ejemplo_nota}: {nota_texto(ejemplo_nota)}")

    cuenta_atras(3)

    saluda_clientes(["Ana", "Luis", "Marta"])
