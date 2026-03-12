# Sistema de Gestión de Inventario 📦

Este es un programa de consola desarrollado en **Python** diseñado para administrar el inventario de productos de forma sencilla. Permite registrar artículos, calcular totales automáticamente y generar reportes de existencias.

## 🚀 Características
*   **Interfaz de menú:** Navegación intuitiva mediante opciones numéricas.
*   **Gestión de productos:** Registro de nombre, precio unitario y cantidad.
*   **Cálculos automáticos:** El sistema calcula el valor total (`cantidad * precio`) por cada entrada.
*   **Manejo de Errores:** Validaciones con `try-except` para evitar cierres inesperados ante datos inválidos.

## 🛠️ Requisitos
*   **Python 3.10** o superior (necesario para el uso de la estructura `match-case`).

## 📂 Estructura del Proyecto
Para que el código funcione correctamente, asegúrate de mantener esta estructura de carpetas:
```text
.
├── main.py                # Código principal (punto de entrada)
└── src/
    └── product_functions.py # Módulo con add_product, view_inventory y generate_report
