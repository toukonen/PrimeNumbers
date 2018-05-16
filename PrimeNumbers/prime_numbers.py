import time
import os
import csv

"""
Class for prime numbers and prime factors calculation
"""
class PrimeNumbers():
    def __init__(self):
        self.primes = [2]
        self.max_prime = 2
        self.save_file_name = ''
        self.saved_primes_file = 'primes.dat'
        self.last_prime_factor = []

        self.read_primes()


    """
    Write found prime numbers to file
    """
    def write_primes(self):
        try:
            # create and clear database file
            open(self.saved_primes_file, "w").close()

            # Write prime factors to csv file
            with open(self.saved_primes_file, 'w') as file:
                writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE)
                writer.writerow(self.primes)
        except Exception as e:
            print(str(e))
            self.primes = [2]

    """
    Read saved prime numbers from csv file to list
    """
    def read_primes(self):
        try:
            # create file if not exist
            if not os.path.exists(self.saved_primes_file):
                open(self.saved_primes_file, "w").close()

            # Read prime numbers from csv file
            with open(self.saved_primes_file, 'r') as file:
                try:
                    reader = csv.reader(file,delimiter=',',quoting=csv.QUOTE_NONE)
                    self.primes = []

                    for row in reader:
                        self.primes = list(map(int, row))
                        break

                except Exception as e:
                    print(str(e))

            # Get highest value (last)
            self.max_prime = 2
            if len(self.primes) > 0:
                self.max_prime = self.primes[len(self.primes)-1]

        except Exception as e:
            print(str(e))
            self.primes = [2]

    """
    Set file name for result print (optionally)
    """
    def set_res_file(self, filename):
        self.save_file_name = filename

    """
    Write result to file if filename defined
    """
    def write_res_to_file(self, primes, max_num, time):
        try:
            if self.save_file_name is not '':
                with open(self.save_file_name, 'w') as file:
                    file.truncate()
                    file.write('Prime Factors of number '+str(max_num)+' are:\n')
                    for num in primes:
                        file.write(str(num)+'\n')
                    file.write('It took '+"{0:.2f}".format(time)+' seconds to find those')
        except Exception as e:
            print(str(e))

    """
    Calculate all prime number from 2 to given value
    """
    def calc_all_primes(self, num_max):
        # Calculate new values (Only numbers which not in db file)
        for i in range(self.max_prime,num_max):
            self.is_prime(i)

    """
    Calculate all prime factors for a given number
    """
    def calc_all_prime_factors(self, num):
        print('Prime Factors of number ' + str(num) + ' are:')
        self.last_prime_factor = []
        start = time.time()

        self.calc_all_primes(num) # Generate a list of prime numbers

        for i in self.primes:
            if num%i == 0:
                print('Prime factor found ' + str(i))
                self.last_prime_factor.append(i)
            if i >= num/2:
                break
        end = time.time()
        t = end-start
        try:
            print('It took ' + "{0:.2f}".format(t) + ' seconds to find those')
            self.write_res_to_file(self.last_prime_factor, num, end - start)
            self.write_primes()
        except Exception as e:
            print(str(e))


    """
    Check is prime number
    """
    def is_prime(self, num):
        try:
            if num%2 == 0:
                return False # Only odd numbers can be prime (except 2, which is handled separately)

            # Loop all founded prime numbers in increasing order
            for i in self.primes:
                try:
                    if i == num:
                        return True # prime already defined

                    div, rem = divmod(num, int(i))
                    if rem == 0:
                        return False # Number is divisible with other prime number
                    elif div < int(i) or i > num:
                        break        # Number is divisible only by itself
                except Exception as e:
                    print(str(e))

            # Add to list if not exist
            if num > self.max_prime:
                self.primes.append(int(num))
                self.max_prime = num
            return True
        except Exception as e:
            print(str(e))
        return False
