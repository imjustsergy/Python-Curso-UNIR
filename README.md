# Python-Curso-UNIR
UNIR - Curso de Python

## Entorno de desarrollo

El curso se desarrolla con Python 3.8. El repositorio usa [uv](https://docs.astral.sh/uv/) para gestionar el intérprete y las dependencias reproducibles.

```bash
uv sync
uv run python --version
```

El segundo comando debe mostrar una versión de Python 3.8. Para ejecutar una actividad, usa el mismo entorno:

```bash
uv run python calculadora_promedios.py
```
