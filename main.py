from app import Product, ShoppingCart
laptop = Product ("Macbook Pro", 1299.98, 123456)
headphones = Product ("Solo 4", 149.99, 983654) 


print (laptop)
print (headphones)
cart = ShoppingCart()

cart.add_items(laptop)
cart.add_items(headphones, 3)   

print (cart.items)
print (cart)

cart.display_cart()