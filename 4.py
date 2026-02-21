
from datetime import datetime

try:
    birth_year = int(input("Enter your birth year: "))
    current_year = datetime.now().year

    age = current_year - birth_year

    # Calculations
    print("\nAge Details:")
    print("Age in years:", age)
    print("Age in months:", age * 12)
    print("Age in days (approx):", age * 365)
    print("Age in hours:", age * 365 * 24)
    print("Age in minutes:", age * 365 * 24 * 60)
    print("Years until 100:", 100 - age if age < 100 else 0)

except ValueError:
    print("Please enter a valid year.")