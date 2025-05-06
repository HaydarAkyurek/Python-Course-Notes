# Define a metaclass that customizes attribute names
class Meta(type):
    def __new__(cls, class_name, bases, attrs):
        # Print the original attributes of the class being created
        print(attrs)  # Dictionary of attributes and methods defined in the class

        modified_attrs = {}  # New dictionary to store modified attribute names

        for name, value in attrs.items():
            # If the attribute name starts with an underscore (private/protected)
            if name.startswith("_"):
                modified_attrs[name] = value  # Keep it as is
            else:
                modified_attrs[name.upper()] = value  # Convert attribute name to uppercase

        # Create the new class with modified attributes
        return super().__new__(cls, class_name, bases, modified_attrs)

# Define a class using the Meta metaclass
class Person(metaclass=Meta):
    x = 5  # Attribute 'x'
    y = 10  # Attribute 'y'
    _age = 40  # Attribute '_age' (protected)

    def hello(self):
        # Method to print a greeting
        print("Hello")

# Create an instance of Person
person_instance = Person()

# Access modified attributes (they are uppercase due to metaclass logic)
result = person_instance.X  # Access original 'x' as 'X'
result = person_instance.Y  # Access original 'y' as 'Y'
result = person_instance._age  # '_age' was kept as is

# Print the last accessed attribute value
print(result)
