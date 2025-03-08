"""
TDD-compliant module for arithmetic operations, Fibonacci calculation (iterative),
and prime factorization with graceful handling for extremely large numbers.

Usage:
    python computations_tdd.py [num1 num2]
"""
import sys
import unittest
import math
import time

def fibonacci_iterative(n):
    """Compute nth Fibonacci number iteratively."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def prime_factors(n, max_runtime=2):
    """
    Compute prime factors of n efficiently, gracefully fail if number too large.
    
    Args:
        n (int): Number to factorize.
        max_runtime (int): Maximum allowed runtime in seconds.
    
    Raises:
        ValueError: If computation is impractical within given constraints.
    """
    start_time = time.time()
    factors = []
    divisor = 2

    while divisor * divisor <= n:
        if time.time() - start_time > max_runtime:
            raise ValueError("Factorization taking too long; number too large.")
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1 if divisor == 2 else 2
    if n > 1:
        factors.append(n)
    return factors

def compute_and_explain(a, b):
    """Perform computations, explaining each step clearly."""
    print(f"Step 1: Adding numbers {a} + {b}")
    added = a + b
    print(f"Result: {added}\n")

    print(f"Step 2: Multiplying numbers {a} * {b}")
    multiplied = a * b
    print(f"Result: {multiplied}\n")

    print("Step 3: Multiplying added result by multiplied result")
    combined = added * multiplied
    print(f"Result: {combined}\n")

    fib_index = combined % 1000
    print(f"Step 4: Computing Fibonacci number at reduced index {fib_index}")
    fib_num = fibonacci_iterative(fib_index)
    print(f"Result: {fib_num}\n")

    print(f"Step 5: Finding prime factors of Fibonacci number {fib_num}")
    try:
        factors = prime_factors(fib_num)
        print(f"Result: {factors}\n")
    except ValueError as e:
        factors = None
        print(f"Failed gracefully: {e}\n")

    return added, multiplied, combined, fib_num, factors

# Unit tests for TDD
class TestComputations(unittest.TestCase):

    def test_fibonacci_iterative(self):
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_iterative(10), 55)
        self.assertEqual(fibonacci_iterative(20), 6765)

    def test_prime_factors_small(self):
        self.assertEqual(prime_factors(60), [2, 2, 3, 5])

    def test_prime_factors_large_fail(self):
        large_number = 10**100 + 1  # Extremely large number
        with self.assertRaises(ValueError):
            prime_factors(large_number, max_runtime=1)

    def test_compute_and_explain(self):
        added, multiplied, combined, fib_num, factors = compute_and_explain(3, 4)
        self.assertEqual(added, 7)
        self.assertEqual(multiplied, 12)
        self.assertEqual(combined, 84)
        self.assertEqual(fib_num, fibonacci_iterative(84 % 1000))
        self.assertEqual(factors, prime_factors(fib_num))

def main():
    if len(sys.argv) == 3:
        _, a, b = sys.argv
        a, b = int(a), int(b)
    else:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

    # Run unit tests first
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestComputations)
    runner = unittest.TextTestRunner()
    print("\nRunning unit tests...")
    result = runner.run(suite)

    if result.wasSuccessful():
        print("\nAll tests passed! Proceeding to computations:\n")
        compute_and_explain(a, b)
    else:
        print("\nTests failed. Fix issues before proceeding.")

if __name__ == "__main__":
    main()
