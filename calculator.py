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
def pow(a,b):
    return a**b
def main():
    print("\n🔢 Welcome to CLI Calculator")
    print("""
🧮 Welcome to CLI Calculator!

Here’s how to use it:

➕  Add:         Type `add` to perform addition
➖  Subtract:    Type `sub` to perform subtraction
✖️  Multiply:    Type `mul` to perform multiplication
➗  Divide:      Type `div` to perform division

📥 Input: You'll be asked to enter two numbers
📤 Output: The calculator will display the result

🔁 To calculate again: Just follow the prompts
❌ To exit: Type `exit` at any time

Let’s get calculating!
You are the BEST !
""")
    print("Choose operation: add, subtract, multiply, divide, pow ")
    operation = input("Operation: ").strip().lower()

    if operation not in ['add', 'subtract', 'multiply', 'divide','pow']:
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
    elif operation == 'pow':
        result = num1 ** num2
    print(f"✅ Result: {result}")

if __name__ == "__main__":
    main()
