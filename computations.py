"""
Module for arithmetic and number theory operations.
"""

def fibonacci(n):
    """Calculate the nth Fibonacci number using memoization."""
    memo = {0: 0, 1: 1}
    def fib(n):
        if n in memo:
            return memo[n]
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    return fib(n)

def prime_factors(n):
    """Calculate all prime factors of a given number."""
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def compute_and_explain(a, b, fib_n):
    """Perform computations and explain each step."""
    added = a + b
    multiplied = a * b
    combined = added * multiplied
    fib_num = fibonacci(fib_n)
    factors = prime_factors(fib_num)

    print(f"Added {a} and {b}: {added}")
    print(f"Multiplied {a} and {b}: {multiplied}")
    print(f"Combined result (added * multiplied): {combined}")
    print(f"{fib_n}th Fibonacci number: {fib_num}")
    print(f"Prime factors of {fib_num}: {factors}")

# Tests
def test():
    assert fibonacci(10) == 55, "Fibonacci function failed"
    assert prime_factors(55) == [5, 11], "Prime factorization failed"
    print("All tests passed.")

if __name__ == "__main__":
    test()
    compute_and_explain(3, 4, 10)
