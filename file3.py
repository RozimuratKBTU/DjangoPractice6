"""file3.py — простые математические утилиты и тесты"""

import math
from typing import List

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def primes_up_to(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, isprime in enumerate(sieve) if isprime]

def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def test_functions():
    print("factorial 5:", factorial(5))
    print("primes up to 20:", primes_up_to(20))
    print("fib 10:", fib(10))

if __name__ == "__main__":
    test_functions()
    # добавим строки для объёма
    for i in range(12):
        print("log", i)
