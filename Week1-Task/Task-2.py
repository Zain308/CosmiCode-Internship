# Cosmicode Week 1 Task 2: Advanced Arithmetic Operations
def calculate_power(base, exponent):
    """Calculate the power of a number (base^exponent)."""
    if not (isinstance(base, (int, float)) and isinstance(exponent, (int, float))):
        return "Error: Inputs must be numbers."
    return base ** exponent

def calculate_modulo(dividend, divisor):
    """Calculate the modulo (remainder) of dividend % divisor."""
    if not (isinstance(dividend, (int, float)) and isinstance(divisor, (int, float))):
        return "Error: Inputs must be numbers."
    if divisor == 0:
        return "Error: Division by zero is not allowed."
    return dividend % divisor

# Main program with user interaction
print("Welcome to the Advanced Arithmetic Calculator!")
print("This program calculates power (x^y) and modulo (x % y).")

while True:
    try:
        # Get user input
        base = float(input("Enter the base number: "))
        exp = float(input("Enter the exponent for power (x^y): "))
        div = float(input("Enter the dividend for modulo (x % y): "))
        mod = float(input("Enter the divisor for modulo (x % y): "))

        # Calculate and display results
        power_result = calculate_power(base, exp)
        modulo_result = calculate_modulo(div, mod)

        print(f"\nResults:")
        print(f"{base} raised to the power of {exp} = {power_result}")
        print(f"{div} modulo {mod} = {modulo_result}")

        # Ask to continue
        again = input("\nCalculate again? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the calculator!  Goodbye!")
            break

    except ValueError:
        print("Error: Please enter valid numerical values.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Program ended.")