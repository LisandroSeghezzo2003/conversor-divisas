
from tabulate import tabulate

from logica import validar_monto


def pedir_monto() -> float:
    """Pide un monto en pesos hasta que el usuario escriba uno valido"""

    while True:
        texto = input("Ingrese un monto en pesos argentinos (ARS): ")
        try:
            return validar_monto(texto)
        except ValueError:
            print("[X] Monto invalido. Ingrese un numero mayor que cero.")

def mostrar_tabla(filas: list[list], monto: float) -> None:
    """Muestra la tabla con los resultados """

    encabezados = ["Dolar", "Compra", "Venta", "Total en USD"]

    print(f"\nConversion de $ {monto:.2f} ARS\n")

    tabla = tabulate(
        filas,
        headers=encabezados,
        floatfmt=".2f",
        tablefmt="rounded_grid",
    )

    print(tabla)
