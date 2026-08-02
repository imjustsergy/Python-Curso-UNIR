# Python-Curso-UNIR
UNIR - Curso de Python

## Entorno de desarrollo

El curso se desarrolla con Python 3.8. El repositorio usa [uv](https://docs.astral.sh/uv/) para gestionar el intérprete y las dependencias reproducibles.

```bash
uv sync
uv run python --version
```

El segundo comando debe mostrar una versión de Python 3.8. Cada carpeta incluye una explicación y los recursos de su entrega:

| Actividad | Contenido |
| --- | --- |
| [Trabajo 1 · Sintaxis Python](trabajo-1-sintaxis-python/README.md) | Calculadora interactiva de promedios escolares. |
| [Trabajo 2 · POO](trabajo-2-poo-inventario/README.md) | Sistema de inventario basado en clases. |
| [Trabajo 3 · NumPy y Pandas](trabajo-3-analisis-datos-numpy-pandas/README.md) | Notebook de análisis de ventas, inventario y satisfacción. |
| [Trabajo 4 · Matplotlib y Seaborn](trabajo-4-visualizacion-matplotlib-seaborn/README.md) | Análisis visual del dataset Superstore. |

Por ejemplo, para ejecutar una actividad interactiva:

```bash
uv run python trabajo-1-sintaxis-python/calculadora_promedios.py
```
