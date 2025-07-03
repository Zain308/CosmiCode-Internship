def fibonacci_iterative(n):
    """Generate the first n Fibonacci numbers using an iterative approach."""
    if n <= 0:
        return []
    
    fib = [0, 1] if n > 1 else [0] if n == 1 else []
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def fibonacci_recursive(n):
    """Generate the first n Fibonacci numbers using a recursive approach."""
    def fib_calc(k):
        if k <= 1:
            return k
        return fib_calc(k-1) + fib_calc(k-2)
    
    return [fib_calc(i) for i in range(n)] if n > 0 else []

def main():
    n = 30  # Number of Fibonacci numbers to generate
    try:
        # Generate Fibonacci numbers using iterative approach
        iterative_result = fibonacci_iterative(n)
        print(f"First {n} Fibonacci numbers (Iterative): {iterative_result}")
        
        # Generate Fibonacci numbers using recursive approach
        recursive_result = fibonacci_recursive(n)
        print(f"First {n} Fibonacci numbers (Recursive): {recursive_result}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()