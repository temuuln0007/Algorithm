import unittest

def count_primes(n):
    if n < 2:
        return 0, []  

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False 
    #print("is_prime:", is_prime)

    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    #print(is_prime)
    prime_numbers = []
    for i, prime in enumerate(is_prime):
        if prime:
            prime_numbers.append(i)

    return len(prime_numbers), prime_numbers

n = 18
count, primes = count_primes(n)
print(f"{n} тоо хүртэл анхний тоо {count}: {primes}")

class TestCountPrimes(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(count_primes(1), (0, [])) 
        self.assertEqual(count_primes(2), (1, [2])) 
        self.assertEqual(count_primes(10), (4, [2, 3, 5, 7]))  

    def test_medium_numbers(self):
        self.assertEqual(count_primes(18), (7, [2, 3, 5, 7, 11, 13, 17])) 
        self.assertEqual(count_primes(30), (10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]))  

    def test_large_numbers(self):
        self.assertEqual(count_primes(100)[0], 25)  
        self.assertIn(97, count_primes(100)[1])  

    def test_edge_cases(self):
        self.assertEqual(count_primes(0), (0, []))  
        self.assertEqual(count_primes(-5), (0, [])) 

unittest.main()
