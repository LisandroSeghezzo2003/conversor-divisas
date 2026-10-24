
import requests

URL = "https://dolarapi.com/v1/dolares"


def validar_monto(texto: str) -> float:
    """Convierte el texto ingresado en un monto valido """

    monto = float(texto.replace(",", "."))
    if monto <= 0:
        raise ValueError("[X] El monto debe ser mayor que cero.")
    return monto


def obtener_cotizaciones() -> list[dict]:
    """Consulta a la API las cotizaciones del dolar """
    try:
        respuesta = requests.get(URL, timeout=10)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.ConnectionError:
        raise Exception("[X] No hay conexion a internet.")
    except requests.RequestException:
        raise Exception("[X] No se pudo consultar la API.")


def calcular_conversiones(cotizaciones: list[dict], monto: float) -> list[list]:
    """Convierte el monto a dolar oficial y blue """

    filas = []
    try:
        for cotizacion in cotizaciones:
            if cotizacion["casa"] in ("oficial", "blue"):
                compra = float(cotizacion["compra"])
                venta = float(cotizacion["venta"])
                total = monto / venta # Se divide por el precio de venta porque es el que paga quien compra
                filas.append([cotizacion["nombre"], compra, venta, total])

    except (KeyError, TypeError, ValueError, ZeroDivisionError):
        raise Exception("[X] La API devolvió datos incompletos.")

    if not filas:
        raise Exception("[X] La API no devolvió el dólar oficial ni el blue.")
    return filas
