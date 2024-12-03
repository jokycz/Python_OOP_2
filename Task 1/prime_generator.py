from TimerAdapter import timer_adapter


class PrimeGenerator:
    def __init__(self, max_number=1000):
        self.max_number = max_number

    def is_prime(self, number):
        # Oprava: čísla menší než 2 nejsou prvočísla
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    @timer_adapter
    def generate_primes(self):
        primes = []
        for num in range(2, self.max_number + 1):  # Startujeme od 2, protože 0 a 1 nejsou prvočísla
            if self.is_prime(num):
                primes.append(num)
        return primes

    @timer_adapter
    def generate_primes_in_range(self, start, end):
        if start > end:
            raise ValueError("Začátek intervalu musí být menší nebo rovný konci.")
        primes = []
        for num in range(max(2, start), end + 1):  # Startujeme od 2, protože 0 a 1 nejsou prvočísla
            if self.is_prime(num):
                primes.append(num)
        return primes