"""Visualizaciones de ventas minoristas con Matplotlib y Seaborn."""

from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns


ARCHIVO_DATOS = Path("superstore_dataset2012.csv")
ARCHIVO_SUBPLOTS = Path("visualizaciones_superstore.png")
ARCHIVO_HEATMAP = Path("heatmap_correlaciones.png")


def cargar_y_preparar_datos(ruta):
    """Carga el CSV, convierte fechas y comprueba los campos necesarios."""
    datos = pd.read_csv(ruta)
    columnas_requeridas = {
        "Order Date", "Category", "Sales", "Profit", "Quantity", "Discount"
    }
    faltantes = columnas_requeridas - set(datos.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas necesarias: {sorted(faltantes)}")

    datos["Order Date"] = pd.to_datetime(datos["Order Date"], dayfirst=True, errors="coerce")
    datos = datos.dropna(subset=["Order Date", "Category", "Sales", "Profit"])
    return datos


def crear_visualizaciones(datos):
    """Genera y guarda cuatro gráficos requeridos en una figura de subplots."""
    sns.set_theme(style="whitegrid", palette="deep")
    fig, ejes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle("Análisis visual de ventas minoristas Superstore", fontsize=16, fontweight="bold")

    # Matplotlib univariante: permite ver que la mayoría de pedidos tiene ventas bajas.
    ejes[0, 0].hist(datos["Sales"], bins=40, color="#0057b8", edgecolor="white")
    ejes[0, 0].set_title("Distribución de ventas (Matplotlib)")
    ejes[0, 0].set_xlabel("Ventas")
    ejes[0, 0].set_ylabel("Frecuencia")

    # Seaborn univariante: compara dispersión y valores atípicos de beneficio por categoría.
    sns.boxplot(data=datos, x="Category", y="Profit", hue="Category", legend=False, ax=ejes[0, 1])
    ejes[0, 1].set_title("Beneficio por categoría (Seaborn)")
    ejes[0, 1].set_xlabel("Categoría")
    ejes[0, 1].set_ylabel("Beneficio")
    ejes[0, 1].tick_params(axis="x", rotation=12)

    # Matplotlib bivariante: muestra la relación entre ventas y beneficio por pedido.
    colores = np.where(datos["Profit"] >= 0, "#0f766e", "#b91c1c")
    ejes[1, 0].scatter(datos["Sales"], datos["Profit"], c=colores, alpha=0.45, s=18)
    ejes[1, 0].axhline(0, color="#333333", linewidth=0.8)
    ejes[1, 0].set_title("Ventas frente a beneficio (Matplotlib)")
    ejes[1, 0].set_xlabel("Ventas")
    ejes[1, 0].set_ylabel("Beneficio")

    # Seaborn bivariante: resume los ingresos medios de cada categoría.
    sns.barplot(data=datos, x="Category", y="Sales", estimator="mean", errorbar=None, ax=ejes[1, 1])
    ejes[1, 1].set_title("Venta media por categoría (Seaborn)")
    ejes[1, 1].set_xlabel("Categoría")
    ejes[1, 1].set_ylabel("Ventas medias")
    ejes[1, 1].tick_params(axis="x", rotation=12)

    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(ARCHIVO_SUBPLOTS, dpi=160, bbox_inches="tight")
    plt.close(fig)


def crear_heatmap(datos):
    """Crea una visualización multivariante de correlaciones con Seaborn."""
    columnas_numericas = ["Sales", "Profit", "Quantity", "Discount", "Shipping Cost"]
    correlacion = datos[columnas_numericas].corr(numeric_only=True)
    fig, eje = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlacion, annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=eje)
    eje.set_title("Correlación entre variables numéricas (Seaborn)")
    fig.tight_layout()
    fig.savefig(ARCHIVO_HEATMAP, dpi=160, bbox_inches="tight")
    plt.close(fig)


def main():
    """Ejecuta la preparación, análisis descriptivo y generación de gráficos."""
    datos = cargar_y_preparar_datos(ARCHIVO_DATOS)
    crear_visualizaciones(datos)
    crear_heatmap(datos)

    print(f"Filas analizadas: {len(datos)}")
    print(f"Nulos restantes en columnas usadas: {datos[['Order Date', 'Category', 'Sales', 'Profit']].isna().sum().sum()}")
    print(f"Venta media: {datos['Sales'].mean():.2f}")
    print(f"Beneficio medio: {datos['Profit'].mean():.2f}")
    print(f"Figura de subplots guardada: {ARCHIVO_SUBPLOTS}")
    print(f"Heatmap guardado: {ARCHIVO_HEATMAP}")


if __name__ == "__main__":
    main()
