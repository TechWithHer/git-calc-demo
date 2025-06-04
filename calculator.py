# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

def main():
    print("\n🔢 Welcome to CLI Calculator")
    print("Choose operation: add, subtract, multiply, divide")
    operation = input("Operation: ").strip().lower()

    if operation not in ['add', 'subtract', 'multiply', 'divide']:
        print("❌ Invalid operation")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")
        return

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)

    print(f"✅ Result: {result}")

if __name__ == "__main__":
    main()
