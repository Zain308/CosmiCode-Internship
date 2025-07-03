def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b using Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate the Least Common Multiple of a and b."""
    if a == 0 or b == 0:
        return 0  # LCM is undefined for zero
    return abs(a * b) // gcd(a, b)

def main():
    try:
        # Get input from user
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
        
        # Calculate GCD and LCM
        gcd_result = gcd(a, b)
        lcm_result = lcm(a, b)
        
        # Display results
        print(f"GCD of {a} and {b}: {gcd_result}")
        if lcm_result == 0:
            print("LCM is undefined when either number is zero.")
        else:
            print(f"LCM of {a} and {b}: {lcm_result}")
            
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()