# Conversor de Divisas (ARS a USD)
Programa de consola que convierte un monto en pesos argentinos (ARS) a
dólar oficial y dólar blue, usando la cotización actual de la API pública
[DolarAPI](https://dolarapi.com/v1/dolares).
El resultado se muestra en una tabla con: nombre del dólar, compra, venta y
total convertido en dólares.

La conversión se calcula con el precio de "venta", porque es el que paga y quien compra dólares.

**Integrantes:** Martín Lazzaro - Ludueña Nicolas - Seghezzo Lisandro, Martin

## Estructura del proyecto

El código está dividido en tres archivos, cada uno con una tarea:

`main.py` Programa principal. Es el que se ejecuta y conecta las otras dos partes. |
`logica.py` Valida el monto, consulta la API y calcula las conversiones. |
`vista.py` Pide el monto al usuario y muestra la tabla. |
`requirements.txt` Lista de librerías que hay que instalar. |
`.gitignore` Indica a Git qué archivos no subir (entorno virtual, caché). |

## Requisitos

- Python 3.9 o superior
- Librerías: `requests` (consulta la API) y `tabulate` (arma la tabla)

## Instalación
1. Abrí una terminal y entrá a la carpeta del proyecto:

   ```bash
   cd conversor_divisas
   ```

2. Creá el entorno virtual (una "caja" aislada para las librerías del
   proyecto):

   ```bash
   python -m venv .venv
   ```

3. Activalo:

   - Windows: `.venv\Scripts\activate`
   - Linux / Mac: `source .venv/bin/activate`

4. Instalá las librerías:

   ```bash
   pip install -r requirements.txt
   ```

## Cómo ejecutarlo

```bash
python main.py
```

El programa te pide el monto en pesos y muestra la tabla:

```
Ingrese un monto en pesos argentinos (ARS): 1000000
Consultando cotizaciones...

Conversion de $ 1000000.00 ARS

╭─────────┬──────────┬─────────┬────────────────╮
│ Dolar   │   Compra │   Venta │   Total en USD │
├─────────┼──────────┼─────────┼────────────────┤
│ Oficial │      ... │     ... │            ... │
│ Blue    │      ... │     ... │            ... │
╰─────────┴──────────┴─────────┴────────────────╯
```

(Los valores reales dependen de la cotización del día.)

## Qué errores controla

- **Monto inválido** (letras, cero o negativo): avisa y vuelve a pedirlo.
- **Sin internet o API caída:** muestra un mensaje de error.
- **Datos incompletos de la API:** muestra un mensaje de error.
- **Cancelación con Ctrl+C:** termina el programa sin errores.

Podés escribir los decimales con coma o con punto (`1500,50` o `1500.50`).
No uses separador de miles (escribí `1500000`, no `1.500.000`).