from prime_numbers import PrimeNumbers

"""
Main program
"""
if __name__ == '__main__':
    try:
        # Init prime number class (Read calculated prime numbers from file)
        prime = PrimeNumbers()

        # Ask value for prime factor calculation
        var = int(input("Give me the number:"))

        # Set result file
        prime.set_res_file('res.txt')

        # Calculate all prime factors for a number defined by user
        prime.calc_all_prime_factors(var)
    except Exception as e:
        print(str(e))


