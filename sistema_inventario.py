"""Sistema interactivo y básico de gestión de inventario."""

from math import isfinite


class Producto:
    """Representa un producto con nombre, precio unitario y cantidad."""

    def __init__(self, nombre, precio, cantidad):
        self.nombre = self._validar_nombre(nombre)
        self.precio = self._validar_precio(precio)
        self.cantidad = self._validar_cantidad(cantidad)

    @staticmethod
    def _validar_nombre(nombre):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre del producto no puede estar vacío.")
        return nombre

    @staticmethod
    def _validar_precio(precio):
        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número.")
        precio = float(precio)
        if not isfinite(precio) or precio < 0:
            raise ValueError("El precio debe ser un número mayor o igual que cero.")
        return precio

    @staticmethod
    def _validar_cantidad(cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que cero.")
        return cantidad

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio tras validar que sea válido."""
        self.precio = self._validar_precio(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad tras validar que sea válida."""
        self.cantidad = self._validar_cantidad(nueva_cantidad)

    def calcular_valor_total(self):
        """Devuelve el valor del stock de este producto."""
        return self.precio * self.cantidad

    def __str__(self):
        return (
            f"{self.nombre} | Precio: {self.precio:.2f} € | "
            f"Cantidad: {self.cantidad} | Valor: {self.calcular_valor_total():.2f} €"
        )


class Inventario:
    """Gestiona una colección de objetos Producto."""

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        """Añade un producto válido al inventario."""
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden añadir objetos de tipo Producto.")
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        """Busca un producto por nombre exacto sin distinguir mayúsculas."""
        if not isinstance(nombre, str):
            raise TypeError("El nombre de búsqueda debe ser una cadena de texto.")
        nombre = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre:
                return producto
        return None

    def calcular_valor_inventario(self):
        """Suma el valor total de todos los productos almacenados."""
        return sum(producto.calcular_valor_total() for producto in self.productos)

    def listar_productos(self):
        """Muestra los productos del inventario por consola."""
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("\n--- Productos en inventario ---")
        for producto in self.productos:
            print(producto)


def menu_principal(inventario):
    """Muestra el menú y procesa operaciones hasta que el usuario sale."""
    while True:
        print("\n--- Menú de inventario ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        opcion = input("Selecciona una opción: ").strip()

        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: ").strip().replace(",", "."))
                cantidad = int(input("Cantidad: ").strip())
                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("Producto agregado correctamente.")
            elif opcion == "2":
                nombre = input("Nombre exacto del producto: ")
                producto = inventario.buscar_producto(nombre)
                if producto is None:
                    raise LookupError("Producto no encontrado.")
                print(f"Producto encontrado: {producto}")
            elif opcion == "3":
                inventario.listar_productos()
            elif opcion == "4":
                valor = inventario.calcular_valor_inventario()
                print(f"Valor total del inventario: {valor:.2f} €")
            elif opcion == "5":
                print("Gracias por usar el sistema de inventario.")
                break
            else:
                print("Opción no válida. Selecciona un número del 1 al 5.")
        except (TypeError, ValueError) as error:
            print(f"Datos no válidos: {error}")
        except LookupError as error:
            print(error)


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)
