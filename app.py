class Product:
    def __init__(self, name, price, sku):
        self.name = name
        self.price = price
        self.sku = sku

    def __str__(self):
        return f"{self.name} (SKU: {self.sku}) - ${self.price:.2f}"


class ShoppingCart:
    #define the constructor
    def __init__(self):
        self.items = []

    #define the __str__ method
    def __str__(self):
        return f"Shopping Cart with {len(self.items)} items."
    #define the add_items method
    def add_items(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def get_total(self):
        #initialize total to 0
        total = 0


        #loop through the items in the cart and sum up the values
        for item in self.items:
            total += item["product"].price * item["quantity"]



        #return the total
        return total

    def display_cart(self):
        #interate through the items in the cart and print them out
        for item in self.items:
           print(f"{item['product']} - Quantity: {item['quantity']}")

        print(f"Total: ${self.get_total():.2f}")