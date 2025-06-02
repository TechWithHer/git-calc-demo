def add(a, b):
    return a + b

#<<<<<<< HEAD
def multiply(a, b):
    return a * b
#=======
def subtract(a, b):
    return a - b
#>>>>>>> 3d02467 ( Add subtraction feature)

def main():
    print("Simple Calculator")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"Sum: {add(x, y)}")
#<<<<<<< HEAD
    print(f"Product: {multiply(x, y)}")
#=======
    print(f"Difference: {subtract(x, y)}")
#>>>>>>> 3d02467 ( Add subtraction feature)

if __name__ == "__main__":
    main()

