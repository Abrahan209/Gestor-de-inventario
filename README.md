# 1. Descripción General

Este sistema permite gestionar un inventario de productos a través de operaciones como:

- Agregar productos
- Actualizar cantidades
- Eliminar productos
- Calcular el valor total del inventario

El sistema es implementado en Python y cuenta con pruebas unitarias para validar su correcto funcionamiento.

# 2. Casos de Uso

## Agregar un Producto

Permite añadir un nuevo producto al inventario con nombre, cantidad y precio.

## Actualizar la Cantidad de un Producto

Modifica la cantidad de un producto existente en el inventario.

## Eliminar un Producto

Elimina un producto del inventario si existe.

## Consultar el Valor Total del Inventario

Calcula y muestra el valor total del inventario basado en cantidad y precio de los productos.

# 3. Implementación del Código

## 3.1 inventario.py (Código Principal)

El código principal implementa las clases Inventory y Product.

    class Product:
        def __init__(self, name, quantity, price):
            self.name = name
            self.quantity = quantity
            self.price = price
    
    class Inventory:
        def __init__(self):
            self.products = {}

        def add_product(self, name, quantity, price):
            self.products[name] = Product(name, quantity, price)
    
        def update_product_quantity(self, name, quantity):
            if name in self.products:
                if self.products[name].quantity + quantity >= 0:
                    self.products[name].quantity += quantity
                    return True
            return False
    
        def remove_product(self, name):
            return self.products.pop(name, None) is not None
    
        def total_inventory_value(self):
            return sum(p.quantity * p.price for p in self.products.values())

# 4. Pruebas Unitarias

## 4.1 prueba.py

Este archivo contiene las pruebas unitarias utilizando unittest.

    import unittest
    from Inventario import Inventory, Product
    
    class TestInventory(unittest.TestCase):
        def setUp(self):
            self.inventory = Inventory()
            self.inventory.add_product("Laptop", 5, 1200.00)
            self.inventory.add_product("Teclado", 10, 50.00)
    
        def test_add_product(self):
            self.inventory.add_product("Mouse", 7, 25.00)
            self.assertIn("Mouse", self.inventory.products)
            self.assertEqual(self.inventory.products["Mouse"].quantity, 7)
    
        def test_update_product_quantity(self):
            self.inventory.update_product_quantity("Laptop", -2)
            self.assertEqual(self.inventory.products["Laptop"].quantity, 3)
    
        def test_remove_product(self):
            self.assertTrue(self.inventory.remove_product("Teclado"))
            self.assertNotIn("Teclado", self.inventory.products)
    
        def test_total_inventory_value(self):
            total_value = self.inventory.total_inventory_value()
            expected_value = (5 * 1200.00) + (10 * 50.00)
            self.assertEqual(total_value, expected_value)

        if __name__ == "__main__":
            unittest.main()


# 5. Cómo Ejecutar las Pruebas

Para ejecutar las pruebas unitarias, usa el siguiente comando en la terminal:

    python -m unittest Prueba.py
