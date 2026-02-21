
# Part 1: Check if a number is prime
# Part 2: Print prime numbers in a range

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is NOT a prime number.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a PRIME number")
    else:
        print(num, "is NOT a prime number")

# Prime numbers in range
start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")
for n in range(start, end + 1):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            print(n, end=" ")