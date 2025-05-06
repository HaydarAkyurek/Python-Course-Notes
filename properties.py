# There are description and price check properties
# Class to represent a product
class Product:
    def __init__(self, name, price, description):
        # Initialize product name
        self.name = name  # Product name

        # Validate and set price (must be non-negative)
        if price >= 0:
            self._price = price  # Private variable for price
        else:
            raise ValueError("Negative value is not allowed for product price.")

        # Validate and set description (must be < 20 characters)
        if len(description) < 20:
            self.description = description  # Product description
        else:
            raise ValueError("Product description must be less than 20 characters.")

    @property
    def price(self):
        # Getter for price
        return self._price

    @price.setter
    def price(self, value):
        # Setter for price with validation
        if value >= 0:
            self._price = value  # Set new price
        else:
            raise ValueError("Negative value is not allowed for product price.")

# Example usage
product = Product("iPhone 16", 80000, "Apple smartphone")  # Create product with description

print(product.price)  # Print current price

try:
    product.price = -90000  # Attempt to set negative price (will raise error)
except ValueError as e:
    print("Error:", e)

product.price = 70000  # Set new valid price
print(product.name, product.price, product.description)  # Print product details
