def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of Fibonacci terms to generate
        
    Returns:
        list: List of Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence


def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_generator(max_count):
    """
    Generator that yields Fibonacci numbers.
    
    Args:
        max_count (int): Maximum number of Fibonacci numbers to yield
        
    Yields:
        int: Next Fibonacci number
    """
    a, b = 0, 1
    count = 0
    while count < max_count:
        yield a
        a, b = b, a + b
        count += 1


if __name__ == "__main__":
    # Example: Print first 10 Fibonacci numbers
    print("First 10 Fibonacci numbers:")
    print(fibonacci(10))
    
    # Example: Print using generator
    print("\nUsing generator:")
    for num in fibonacci_generator(10):
        print(num, end=" ")
    print()
    
    # Example: Get 8th Fibonacci number (0-indexed)
    print(f"\n8th Fibonacci number: {fibonacci_recursive(8)}")
