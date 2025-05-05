# Class representing an item in the shopping cart after learning Class Constructors, Instance Mothods, 
 # ... Class Attributes, Class Methods
class CartItem:
    discount_rate = 0.8  # Class-level default discount rate (20% discount)
    item_count = 0  # Class-level counter for how many items have been created

    @classmethod
    def display_item_count(cls):
        # Return a string showing how many items have been created
        return f"{cls.item_count} items have been created."

    @classmethod
    def create_item(cls, data_str):
        # Create a CartItem object from a comma-separated string
        name, price, quantity = data_str.split(",")
        return cls(name, float(price), int(quantity))

    def __init__(self, name, price, quantity):
        # Initialize item properties
        self.name = name  # Name of the item
        self.price = price  # Price of the item
        self.quantity = quantity  # Quantity of the item
        CartItem.item_count += 1  # Increment class-level item counter

    def calculate_total(self):
        # Calculate total price for this item
        return self.price * self.quantity

    def apply_discount(self):
        # Apply class-level discount rate to the item price
        self.price = self.price * CartItem.discount_rate

# Class representing a discount coupon
class Coupon:
    def __init__(self, code, discount):
        self.code = code  # Coupon code
        self.discount = discount  # Discount multiplier (e.g., 0.8 means 20% discount)

# Creating coupon instances
coupon1 = Coupon("code1", 0.8)  # 20% discount
coupon2 = Coupon("code2", 0.7)  # 30% discount
coupon3 = Coupon("code3", 0.9)  # 10% discount

# Creating shopping cart items
item1 = CartItem("Phone", 500, 2)
item2 = CartItem("Laptop", 1500, 1)
item3 = CartItem("Book", 30, 3)

# Class representing a shopping cart
class ShoppingCart:
    coupon_list = [coupon1, coupon2, coupon3]  # Available coupons

    def __init__(self, items):
        self.items = items  # List of CartItem objects in the cart

    def add_item(self, item):
        # Add a CartItem object to the cart
        self.items.append(item)

    def display_items(self):
        # Display the name and price of each item in the cart
        for item in self.items:
            print(f"{item.name}: ${item.price}")

    def calculate_totals(self):
        # Calculate total cost of all items in the cart
        return sum([item.calculate_total() for item in self.items])

    def remove_item(self, cart_item):
        # Remove a specific item from the cart
        self.items = [item for item in self.items if item != cart_item]

    def clear(self):
        # Clear all items from the cart
        self.items = []

    @classmethod
    def get_coupons(cls):
        # Return a list of available coupon codes
        return [coupon.code for coupon in cls.coupon_list]

    @classmethod
    def get_coupon(cls, code):
        # Retrieve a coupon object matching the given code
        return next(filter(lambda c: c.code == code, ShoppingCart.coupon_list))

    def apply_coupon(self, code):
        # Apply a coupon discount to all items in the cart
        if code not in ShoppingCart.get_coupons():
            raise ValueError(f"Invalid coupon code: {code}")

        coupon = ShoppingCart.get_coupon(code)

        for index in range(len(self.items)):
            self.items[index].price = self.items[index].price * coupon.discount

    def apply_coupon_to_item(self, code, cart_item):
        # Apply a coupon discount only to a specific item
        if code not in ShoppingCart.get_coupons():
            raise ValueError(f"Invalid coupon code: {code}")

        coupon = ShoppingCart.get_coupon(code)

        # Apply coupon only to the matched item
        for item in self.items:
            if item == cart_item:
                item.price = item.price * coupon.discount
                print(f"Coupon '{code}' applied to item '{item.name}'. New price: ${item.price}")

# Example usage

# Initialize the shopping cart with two items
cart = ShoppingCart([item1, item2])

# Add a third item
cart.add_item(item3)

# Display items before applying coupon
print("\nItems before coupon:")
cart.display_items()

# Print total before applying coupon
print("Total before coupon:", cart.calculate_totals())

# Apply a coupon to the entire cart (30% discount)
cart.apply_coupon("code2")

# Display items and total after applying coupon to entire cart
print("\nItems after applying coupon to entire cart:")
cart.display_items()
print("Total after applying coupon to entire cart:", cart.calculate_totals())

# Now apply a coupon to a single item (10% discount)
cart.apply_coupon_to_item("code3", item3)

# Display items and total after applying coupon to a single item
print("\nItems after applying coupon to a single item (Book):")
cart.display_items()
print("Total after applying coupon to single item:", cart.calculate_totals())
