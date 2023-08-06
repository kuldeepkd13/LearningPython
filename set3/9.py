def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = safe_divide(num1, num2)
print("Result:", result)
