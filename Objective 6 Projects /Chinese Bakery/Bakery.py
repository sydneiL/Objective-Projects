class BreadProduct:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class BreadOrder:
    def __init__(self, customer_name, products):
        self.customer_name = customer_name
        self.products = products

# Example usage:
bread_products = [BreadProduct("Whole Wheat", 2.0, 50), BreadProduct("Baguette", 1.5, 30)]
customer_orders = [BreadOrder("Jane Smith", [BreadProduct("Baguette", 1.5, 2), BreadProduct("Whole Wheat", 2.0, 3)])]


class BakeryGraph:
    def __init__(self):
        self.vertices = {}  # Dictionary to store vertices and their associated data
        self.edges = []     # List to store edges (connections between vertices)

    def add_vertex(self, vertex_id, vertex_data):
        self.vertices[vertex_id] = vertex_data

    def add_edge(self, source, destination, weight):
        self.edges.append((source, destination, weight))

# Example usage:
chinese_bakery = BakeryGraph()

# Add vertices representing products
chinese_bakery.add_vertex("Mooncake", {"type": "Pastry", "price": 3.0})
chinese_bakery.add_vertex("Baozi", {"type": "Bun", "price": 1.5})
chinese_bakery.add_vertex("Dan Ta", {"type": "Dessert", "price": 2.5})

# Add edges representing relationships (e.g., Mooncake supplied by SupplierA)
chinese_bakery.add_edge("SupplierA", "Mooncake", 50)
chinese_bakery.add_edge("SupplierB", "Baozi", 100)
chinese_bakery.add_edge("SupplierC", "Dan Ta", 30)

def sort_products_by_name(products):
    return sorted(products, key=lambda x: x[0])  # Sort by product name

# Example usage:
bakery_products = [("Mooncake", 3.0), ("Baozi", 1.5), ("Dan Ta", 2.5)]
sorted_products = sort_products_by_name(bakery_products)
print("Sorted Products:")
for product in sorted_products:
    print(f"{product[0]}: ${product[1]}")


def search_product_by_price(products, target_price):
    for product in products:
        if product[1] == target_price:
            return product
    return None

# Example usage:
target_price = 1.5
found_product = search_product_by_price(bakery_products, target_price)
if found_product:
    print(f"\nProduct found! {found_product[0]}: ${found_product[1]}")
else:
    print(f"\nNo product found with the price ${target_price}.")


