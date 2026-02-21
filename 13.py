

count = int(input("How many numbers? "))
numbers = []
#taking input
for i in range(count):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
#calculating
print("\nSum:", sum(numbers))
print("Average:", sum(numbers) / count)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))