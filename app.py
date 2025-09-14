class Product:
    def __init__(self, name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id

    def __str__(self):
        return f"{self.name} (SKU: {self.sku}) {self.price:.2f}"


class ShoppingCart:
    pass