import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def list_primes_up_to_n(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a non-negative number.")
            return
        
        # Check if the input number is prime
        if is_prime(n):
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")
        
        # List all prime numbers up to n
        primes = list_primes_up_to_n(n)
        if primes:
            print(f"Prime numbers up to {n}: {primes}")
        else:
            print(f"There are no prime numbers up to {n}.")
            
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()