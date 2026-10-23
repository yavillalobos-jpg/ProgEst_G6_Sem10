# Lista doblemente enlazada

cabeza = None
cola = None


def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}


def agregar_final(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)

    if cabeza is None:
        cabeza = nuevo
        cola = nuevo
    else:
        nuevo["anterior"] = cola
        cola["siguiente"] = nuevo
        cola = nuevo


def mostrar_adelante():
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" -> ")
        actual = actual["siguiente"]
    print("None")


def mostrar_atras():
    actual = cola
    while actual is not None:
        print(actual["dato"], end=" -> ")
        actual = actual["anterior"]
    print("None")


def agregar_inicio(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)

    if cabeza is None:
        cabeza = nuevo
        cola = nuevo
    else:
        nuevo["siguiente"] = cabeza
        cabeza["anterior"] = nuevo
        cabeza = nuevo


def eliminar(dato):
    global cabeza, cola
    actual = cabeza

    while actual is not None and actual["dato"] != dato:
        actual = actual["siguiente"]

    if actual is None:
        return False

    if actual is cabeza:
        cabeza = cabeza["siguiente"]
        if cabeza is not None:
            cabeza["anterior"] = None
        else:
            cola = None
        return True

    if actual is cola:
        cola = cola["anterior"]
        if cola is not None:
            cola["siguiente"] = None
        else:
            cabeza = None
        return True

    actual["anterior"]["siguiente"] = actual["siguiente"]
    actual["siguiente"]["anterior"] = actual["anterior"]
    return True


if __name__ == "__main__":
    agregar_final("Inicio")
    agregar_final("Catálogo")
    agregar_final("Contacto")

    print("Recorrido adelante:")
    mostrar_adelante()

    print("Recorrido atrás:")
    mostrar_atras()

    agregar_inicio("Bienvenida")
    print("Después de agregar al inicio:")
    mostrar_adelante()

    print("Eliminar 'Catálogo':")
    print(eliminar("Catálogo"))
    mostrar_adelante()
    mostrar_atras()
