import random

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def remove_from_cart(self, product):
        self.cart.remove(product)

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products
        self.total_price = sum([p.price for p in products])
        self.id = random.randint(1000, 9999)

class Store:
    def __init__(self):
        self.products = []
        self.orders = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def process_order(self, order):
        self.orders.append(order)
        return order.id

# Example usage:
store = Store()

product1 = Product("T-Shirt", 20, "Comfortable cotton t-shirt")
product2 = Product("Jeans", 50, "Classic denim jeans")
store.add_product(product1)
store.add_product(product2)

customer1 = Customer("John", "john@example.com", "123 Main St")
customer1.add_to_cart(product1)
customer1.add_to_cart(product2)

order1 = Order(customer1, customer1.cart)
order_id = store.process_order(order1)

print(f"Order processed with ID: {order_id}")