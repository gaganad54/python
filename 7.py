
while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
#taking user input
    choice = input("Enter choice: ")
#exit condition
    if choice == "7":
        print("Exiting program.")
        break

    temp = float(input("Enter temperature: "))
#peforming based on user choice
    if choice == "1":
        print("Result:", (temp * 9/5) + 32)
    elif choice == "2":
        print("Result:", (temp - 32) * 5/9)
    elif choice == "3":
        print("Result:", temp + 273.15)
    elif choice == "4":
        print("Result:", temp - 273.15)
    elif choice == "5":
        print("Result:", (temp - 32) * 5/9 + 273.15)
    elif choice == "6":
        print("Result:", (temp - 273.15) * 9/5 + 32)
    else:
        print("Invalid choice!")