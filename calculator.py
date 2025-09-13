def add(x, y):
    """Adds two numbers and returns the result."""
    return x + y
 
def subtract(x, y):
    """Subtracts two numbers and returns the result."""
    return x - y
 
def multiply(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y
 
def divide(x, y):
    """
    Divides two numbers and returns the result.
    Raises a ValueError if the divisor is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
 
if __name__ == "__main__":
    print("This is a simple calculator script.")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"10 / 2 = {divide(10, 2)}")
