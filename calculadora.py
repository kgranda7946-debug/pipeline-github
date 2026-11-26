
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


if __name__ == "__main__":
    print("================================")
    print("     CALCULADORA EN PYTHON")
    print("================================")
    print("Suma: ", sumar(10, 5))
    print("Resta: ", restar(10, 5))
    print("Multiplicacion: ", multiplicar(10, 5))
    print("Division: ", dividir(10, 5))
    print("================================")
