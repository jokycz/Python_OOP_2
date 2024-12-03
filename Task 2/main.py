import sys
from pathlib import Path

# Přidáme cestu k Task 1 na seznam importů
sys.path.append(str(Path(__file__).resolve().parent.parent / "Task 1"))

from prime_generator import PrimeGenerator

if __name__ == "__main__":
    inputFrom = int(input("Zadej začátek intervalu hledání prvočísel:"))
    inputTo = int(input("Zadej konec intervalu hledání prvočísel:"))
    prime_gen = PrimeGenerator(100)
    primes = prime_gen.generate_primes_in_range(inputFrom, inputTo)
    print(f"Prvočísla v  intervalu od {inputFrom} do {inputTo}: {primes}")

