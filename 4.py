class ShoppingCart:
    def __init__(self):
        self.items = []

    def total_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

cart = ShoppingCart()

cart.items.append({'name': 'Laptop', 'price': 1000})
cart.items.append({'name': 'Phone', 'price': 700})
cart.items.append({'name': 'Headphones', 'price': 150})
cart.items.append({'name': 'Keyboard', 'price': 100})
cart.items.append({'name': 'Mouse', 'price': 50})

print(f"Total price of items in cart: ${cart.total_price()}")
