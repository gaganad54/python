

marks = []
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5
passed = all(mark >= 40 for mark in marks)

# Determining grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
#printing resilts
print("\nTotal Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", "Pass" if passed else "Fail")