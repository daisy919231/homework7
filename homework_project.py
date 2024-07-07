

# WITH YIELD, GENERATOR KEYWORD


def prime_numbers(ending_number):
    n = 2
    while n <= ending_number:
        is_prime = True
        for k in range(2, int(n**0.5) + 1):
            if n % k == 0:
                is_prime = False
                break
        if is_prime and n > 1:
            yield n
        n += 1


generator = prime_numbers(100)
limit = 50
try:
    for _ in range(limit):
        print(next(generator))
except StopIteration:
    print('Done!')


# WITH ITERATORS

class Prime:
    def __init__(self, ending_number, limit):
        self.ending_number = ending_number
        self.limit = limit
        self.current_number = 2
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_number <= self.ending_number and self.count < self.limit:
            is_prime = True
            for k in range(2, int(self.current_number**0.5) + 1):
                if self.current_number % k == 0:
                    is_prime = False
                    break
            if is_prime and self.current_number > 1:
                prime = self.current_number
                self.current_number += 1
                self.count += 1
                return prime
            self.current_number += 1
        raise StopIteration

prime_generator = Prime(20, 10) 
for prime in prime_generator:
    print(prime)
