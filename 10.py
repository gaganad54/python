

balance = 10000

while True:
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")
# based on choice
    if choice == "1":
        print("Current Balance: ₹", balance)
#deposit
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful. New balance: ₹", balance)
#withdrawal
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if balance - amount >= 500:
            balance -= amount
            print("Withdrawal successful. New balance: ₹", balance)
        else:
            print("Insufficient balance. Minimum ₹500 must remain.")
#exit
    elif choice == "4":
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid option!")