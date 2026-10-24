"""Programa principal: conecta la logica con la vista."""

import logica
import vista


def main() -> None:
    """Pide el monto, consulta la API y muestra la tabla."""
    try:
        monto = vista.pedir_monto()
        print("Consultando cotizaciones...")
        cotizaciones = logica.obtener_cotizaciones()
        filas = logica.calcular_conversiones(cotizaciones, monto)
        vista.mostrar_tabla(filas, monto)
    except KeyboardInterrupt:
        print("\n [X] Operacion cancelada.")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
