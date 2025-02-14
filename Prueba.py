import unittest
from Inventario import (
    Inventory,
    Product,
)  # Asegúrate de importar las clases correctamente


class TestInventory(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada prueba para iniciar un inventario limpio."""
        self.inventory = Inventory()
        self.inventory.add_product("Laptop", 5, 1200.00)
        self.inventory.add_product("Teclado", 10, 50.00)

    def test_add_product(self):
        """Caso de Uso 1: Verifica que un producto se agregue correctamente."""
        self.inventory.add_product("Mouse", 7, 25.00)
        self.assertIn("Mouse", self.inventory.products)
        self.assertEqual(self.inventory.products["Mouse"].quantity, 7)
        self.assertEqual(self.inventory.products["Mouse"].price, 25.00)

    def test_update_product_quantity(self):
        """Caso de Uso 2: Verifica la actualización de cantidad."""
        self.inventory.update_product_quantity("Laptop", -2)
        self.assertEqual(self.inventory.products["Laptop"].quantity, 3)

        # Intentar restar más de lo disponible
        result = self.inventory.update_product_quantity("Laptop", -5)
        self.assertFalse(result)
        self.assertEqual(
            self.inventory.products["Laptop"].quantity, 3
        )  # No debe cambiar

    def test_remove_product(self):
        """Caso de Uso 3: Verifica la eliminación de productos."""
        self.assertTrue(self.inventory.remove_product("Teclado"))
        self.assertNotIn("Teclado", self.inventory.products)

        # Intentar eliminar un producto que no existe
        self.assertFalse(self.inventory.remove_product("Monitor"))

    def test_total_inventory_value(self):
        """Caso de Uso 4: Verifica el cálculo del valor total del inventario."""
        total_value = self.inventory.total_inventory_value()
        expected_value = (5 * 1200.00) + (10 * 50.00)  # 6000 + 500 = 6500
        self.assertEqual(total_value, expected_value)


if __name__ == "__main__":
    unittest.main()
