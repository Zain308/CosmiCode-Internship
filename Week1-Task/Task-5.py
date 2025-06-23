# Cosmicode Week 1 Task 5: Time Converter
def convert_seconds(total_seconds):
    """Convert total seconds into hours, minutes, and seconds."""
    if not isinstance(total_seconds, (int, float)) or total_seconds < 0:
        return "Error: Please enter a non-negative number of seconds."
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

# Main program with user interaction
print("Welcome to the Time Converter! ⏰")
print("This program converts seconds into hours, minutes, and seconds.")

while True:
    try:
        # Get user input
        seconds = float(input("Enter the time in seconds: "))

        # Convert and display results
        hours, minutes, seconds_remain = convert_seconds(seconds)
        print(f"\nConversion Results:")
        print(f"{int(seconds)} seconds = {int(hours)} hours, {int(minutes)} minutes, "
              f"{int(seconds_remain)} seconds")

        # Ask to continue
        again = input("\nConvert another time? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the Time Converter! 🚀 Goodbye!")
            break

    except ValueError:
        print("Error: Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Program ended.")