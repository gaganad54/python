
try:
    total_bill = float(input("Enter total bill: "))
    people = int(input("Number of people: "))
    tax_percent = float(input("Tax percentage: "))
    tip_percent = float(input("Tip percentage: "))

    # Calculations
    tax_amount = total_bill * (tax_percent / 100)
    after_tax = total_bill + tax_amount
    tip_amount = after_tax * (tip_percent / 100)
    final_bill = after_tax + tip_amount
    per_person = final_bill / people

    # Displaying results
    print("\n=== BILL BREAKDOWN ===")
    print(f"Subtotal:    ₹{total_bill:.2f}")
    print(f"Tax ({tax_percent}%):   ₹{tax_amount:.2f}")
    print(f"After tax:   ₹{after_tax:.2f}")
    print(f"Tip ({tip_percent}%):   ₹{tip_amount:.2f}")
    print(f"Total:       ₹{final_bill:.2f}")
    print(f"Per person:  ₹{per_person:.2f}")
#exceptions
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Number of people cannot be zero.")