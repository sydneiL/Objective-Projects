class CoffeeProduct:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def sort_products_by_price(products):
    return sorted(products, key=lambda x: x.price)

def search_product(products, target_product):
    for product in products:
        if product.name == target_product:
            return product
    return None

# Example usage:
coffee_products = [
    CoffeeProduct("Espresso", 2.5, 100),
    CoffeeProduct("Latte", 3.0, 50),
    CoffeeProduct("Cappuccino", 3.2, 30),
    CoffeeProduct("Americano", 2.8, 40),
]

# Sort coffee products by price
sorted_products = sort_products_by_price(coffee_products)
print("Sorted Products:")
for product in sorted_products:
    print(f"{product.name}: ${product.price}")

# Search for a specific product
target_product = "Latte"
found_product = search_product(coffee_products, target_product)
if found_product:
    print(f"\n{target_product} found! Price: ${found_product.price}, Quantity: {found_product.quantity}")
else:
    print(f"\n{target_product} not found in the inventory.")
