def prime_factors(n):
    """Find all prime factors of a given number n."""
    factors = []
    if n <= 1:
        return factors
    
    # Check for factor 2 separately to optimize for odd numbers later
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check odd numbers up to sqrt(n)
    for p in range(3, int(n**0.5) + 1, 2):
        while n % p == 0:
            factors.append(p)
            n = n // p
    
    # If n is still greater than 1, it is a prime number itself
    if n > 1:
        factors.append(n)
    
    return factors

def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        factors = prime_factors(n)
        if factors:
            print(f"Prime factors of {n}: {factors}")
        else:
            print(f"{n} has no prime factors.")
            
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()