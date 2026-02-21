
# Calculates factorial with step-by-step display

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("0! = 1")
   # fact 0f 0 is 1 
else:
    factorial = 1
    print(f"{num}! =", end=" ")
    for i in range(num, 0, -1):
        factorial *= i
        print(i, end=" x " if i > 1 else "")
    print("=", factorial)