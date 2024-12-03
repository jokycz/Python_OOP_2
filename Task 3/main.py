from DecoratorFactory import DecoratorFactory
from FinancialReport import FinancialReport

# Hlavní část kódu
if __name__ == "__main__":
    # Cesta ke složce dekorátorů
    decorator_directory = "./Decorators"
    base_module = "Decorators"

    # Vytvoření instance factory
    factory = DecoratorFactory(decorator_directory, base_module)

    # Data zprávy
    report_data = {"Revenue": 1000000, "Expenses": 500000, "Profit": 500000}

    # Vytvoření instance FinancialReport
    report = FinancialReport(report_data, factory, "decorator_mapping.json")

    # Generování zpráv pro různé IČO
    print("Report for IČO 12345678:")
    print(report.generate("12345678"))

    print("\nReport for IČO 87654321:")
    print(report.generate("87654321"))

    print("\nReport for IČO 11223344:")
    print(report.generate("11223344"))
