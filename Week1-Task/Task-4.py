# Cosmicode Week 1 Task 4: Area Calculator for Complex Shapes
import math

def calculate_trapezoid_area(a, b, h):
    """Calculate the area of a trapezoid: (a + b) * h / 2."""
    if not all(isinstance(x, (int, float)) for x in [a, b, h]) or h <= 0:
        return "Error: Sides (a, b) must be numbers and height (h) must be positive."
    return (a + b) * h / 2

def calculate_ellipse_area(a, b):
    """Calculate the area of an ellipse: π * a * b."""
    if not all(isinstance(x, (int, float)) for x in [a, b]) or a <= 0 or b <= 0:
        return "Error: Semi-axes (a, b) must be positive numbers."
    return math.pi * a * b

# Main program with user interaction
print("Welcome to the Complex Shape Area Calculator! 🌐")
print("This program calculates the area of a trapezoid or ellipse.")

while True:
    try:
        # Display menu
        print("\nOptions:")
        print("1. Calculate Trapezoid Area")
        print("2. Calculate Ellipse Area")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            a = float(input("Enter the length of first parallel side (a): "))
            b = float(input("Enter the length of second parallel side (b): "))
            h = float(input("Enter the height (h): "))
            result = calculate_trapezoid_area(a, b, h)
            print(f"\nTrapezoid Area: {result} square units")

        elif choice == '2':
            a = float(input("Enter the semi-major axis (a): "))
            b = float(input("Enter the semi-minor axis (b): "))
            result = calculate_ellipse_area(a, b)
            print(f"\nEllipse Area: {result:.2f} square units")

        elif choice == '3':
            print("Thank you for using the Area Calculator! 🚀 Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    except ValueError:
        print("Error: Please enter valid numerical values.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Program ended.")