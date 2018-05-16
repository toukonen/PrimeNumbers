import unittest
from prime_numbers import PrimeNumbers

class TestMethods(unittest.TestCase):

    def test_prime_factor_calculation(self):
        prime = PrimeNumbers()
        var = 13195
        prime.calc_all_prime_factors(var)

        self.assertEqual(prime.last_prime_factor[0], 5)
        self.assertEqual(prime.last_prime_factor[1], 7)
        self.assertEqual(prime.last_prime_factor[2], 13)
        self.assertEqual(prime.last_prime_factor[3], 29)

    def test_file_handling(self):
        # Generate data to file
        prime = PrimeNumbers()
        var = 10
        prime.calc_all_prime_factors(var)

        # Init data from file
        prime = PrimeNumbers()
        self.assertEqual(prime.primes[0], 2)
        self.assertEqual(prime.primes[1], 3)
        self.assertEqual(prime.primes[2], 5)
        self.assertEqual(prime.primes[3], 7)


if __name__ == '__main__':
    unittest.main()