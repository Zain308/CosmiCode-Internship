# Cosmicode Week 1 Task 3: Find Largest and Smallest of Three Numbers
def find_largest_smallest(num1, num2, num3):
    """Find the largest and smallest among three numbers."""
    largest = max(num1, num2, num3)
    smallest = min(num1, num2, num3)
    return largest, smallest

# Main program with user interaction
print("Welcome to the Number Analyzer! 🌟")
print("This program finds the largest and smallest of three numbers.")

while True:
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        # Calculate largest and smallest
        largest, smallest = find_largest_smallest(num1, num2, num3)

        # Display results
        print(f"\nAnalysis Results:")
        print(f"The largest number is: {largest}")
        print(f"The smallest number is: {smallest}")

        # Ask to continue
        again = input("\nAnalyze more numbers? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the Number Analyzer! 🚀 Goodbye!")
            break

    except ValueError:
        print("Error: Please enter valid numerical values.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Program ended.")