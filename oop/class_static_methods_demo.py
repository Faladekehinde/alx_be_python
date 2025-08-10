# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: adds two numbers without accessing class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: accesses class attribute and returns the product."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
