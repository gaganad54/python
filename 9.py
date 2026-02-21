

age = int(input("Enter age: "))
day = input("Enter day of week: ").lower()
tickets = int(input("Number of tickets: "))

# Base price selection
if age < 3:
    price = 0
elif age <= 12:
    price = 150
elif age <= 59:
    price = 300
else:
    price = 200

# Discount logic
discount = 0
if day in ["friday", "saturday", "sunday"]:
    discount = 0.2

final_price = price - (price * discount)
total_amount = final_price * tickets

print("\nBase price:", price)
print("Discount applied:", discount * 100, "%")
print("Price after discount:", final_price)
print("Total amount:", total_amount)