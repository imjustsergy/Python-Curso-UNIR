"""Calculadora interactiva de promedios escolares."""

from math import isfinite


def ingresar_calificaciones():
    """Solicita materias y calificaciones, y devuelve ambas listas."""
    materias = []
    calificaciones = []

    print("Introduce las materias y sus calificaciones (de 0 a 10).")
    while True:
        materia = input("Nombre de la materia: ").strip()
        while not materia:
            print("El nombre de la materia no puede estar vacío.")
            materia = input("Nombre de la materia: ").strip()

        while True:
            entrada = input("Calificación (0-10): ").strip().replace(",", ".")
            try:
                calificacion = float(entrada)
            except ValueError:
                print("Introduce un número válido.")
                continue

            if isfinite(calificacion) and 0 <= calificacion <= 10:
                break
            print("La calificación debe ser un número entre 0 y 10.")

        materias.append(materia)
        calificaciones.append(calificacion)

        while True:
            continuar = input("¿Deseas añadir otra materia? (s/n): ").strip().lower()
            if continuar in ("s", "si", "sí"):
                break
            if continuar in ("n", "no"):
                return materias, calificaciones
            print("Responde con 's' para continuar o 'n' para finalizar.")


def calcular_promedio(calificaciones):
    """Devuelve el promedio de una lista de calificaciones."""
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """Devuelve los índices de las materias aprobadas y reprobadas."""
    aprobadas = []
    reprobadas = []

    for indice, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(indice)
        else:
            reprobadas.append(indice)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """Devuelve los índices de la calificación máxima y mínima."""
    if not calificaciones:
        return None, None
    return calificaciones.index(max(calificaciones)), calificaciones.index(min(calificaciones))


def mostrar_materias(titulo, materias, calificaciones, indices):
    """Muestra las materias indicadas por sus índices."""
    print(titulo)
    if not indices:
        print("  Ninguna")
        return
    for indice in indices:
        print(f"  - {materias[indice]}: {calificaciones[indice]:.2f}")


def main():
    """Ejecuta el flujo principal de la calculadora."""
    materias, calificaciones = ingresar_calificaciones()

    if not materias:
        print("No se ha ingresado ninguna materia.")
        print("¡Gracias por usar la calculadora de promedios!")
        return

    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones)
    indice_maximo, indice_minimo = encontrar_extremos(calificaciones)

    print("\n--- Resumen final ---")
    print("Materias y calificaciones:")
    for materia, calificacion in zip(materias, calificaciones):
        print(f"  - {materia}: {calificacion:.2f}")
    print(f"Promedio general: {promedio:.2f}")
    mostrar_materias("Materias aprobadas:", materias, calificaciones, aprobadas)
    mostrar_materias("Materias reprobadas:", materias, calificaciones, reprobadas)
    print(
        f"Mejor calificación: {materias[indice_maximo]} "
        f"({calificaciones[indice_maximo]:.2f})"
    )
    print(
        f"Peor calificación: {materias[indice_minimo]} "
        f"({calificaciones[indice_minimo]:.2f})"
    )
    print("¡Gracias por usar la calculadora de promedios!")


if __name__ == "__main__":
    main()
