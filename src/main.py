"""Module principal de l'application."""

def add(a, b):
    """Additionne deux nombres."""
    return a + b

def multiply(a, b):
    """Multiplie deux nombres."""
    return a * b

def greet(name):
    """Retourne un message de salutation."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
