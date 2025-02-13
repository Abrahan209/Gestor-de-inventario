class Product:
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount: int):
        """Actualiza la cantidad del producto."""
        if self.quantity + amount >= 0:
            self.quantity += amount
            return True
        return False

    def get_total_value(self):
        """Devuelve el valor total del producto en el inventario."""
        return self.quantity * self.price

    def __repr__(self):
        return f"{self.name}: {self.quantity} unidades, ${self.price:.2f} c/u"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name: str, quantity: int, price: float):
        """Agrega un nuevo producto al inventario."""
        if name in self.products:
            self.products[name].quantity += quantity
        else:
            self.products[name] = Product(name, quantity, price)

    def update_product_quantity(self, name: str, amount: int):
        """Actualiza la cantidad de un producto en el inventario."""
        if name in self.products:
            return self.products[name].update_quantity(amount)
        return False

    def remove_product(self, name: str):
        """Elimina un producto del inventario."""
        return self.products.pop(name, None) is not None

    def list_products(self):
        """Devuelve una lista de todos los productos en el inventario."""
        return list(self.products.values())

    def total_inventory_value(self):
        """Calcula el valor total de todos los productos en el inventario."""
        return sum(product.get_total_value() for product in self.products.values())


def main():
    inventory = Inventory()
    while True:
        print("\n--- Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Actualizar cantidad de producto")
        print("3. Eliminar producto")
        print("4. Listar productos")
        print("5. Ver valor total del inventario")
        print("6. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            name = input("Nombre del producto: ")
            quantity = int(input("Cantidad: "))
            price = float(input("Precio: "))
            inventory.add_product(name, quantity, price)
            print("Producto agregado exitosamente.")

        elif choice == "2":
            name = input("Nombre del producto: ")
            amount = int(input("Cantidad a agregar o restar: "))
            if inventory.update_product_quantity(name, amount):
                print("Cantidad actualizada correctamente.")
            else:
                print("Error: Producto no encontrado o cantidad inválida.")

        elif choice == "3":
            name = input("Nombre del producto a eliminar: ")
            if inventory.remove_product(name):
                print("Producto eliminado correctamente.")
            else:
                print("Error: Producto no encontrado.")

        elif choice == "4":
            products = inventory.list_products()
            if products:
                for product in products:
                    print(product)
            else:
                print("Inventario vacío.")

        elif choice == "5":
            print(f"Valor total del inventario: ${inventory.total_inventory_value():.2f}")

        elif choice == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
