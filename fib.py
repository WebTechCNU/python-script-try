import sys

def fibonacci(n):
    if n <= 0:
        return "Invalid input. n must be a positive integer."

    fib_sequence = [0, 1]
    while len(fib_sequence) <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[n]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fibonacci.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        result = fibonacci(n) + 1
        print(result)
    except ValueError:
        print("Invalid input. Please provide a positive integer value for n.")