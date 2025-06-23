sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))

average = (sub1 + sub2 + sub3) / 3

if 90 <= average <= 100:
    grade = 'A'
elif 80 <= average < 90:
    grade = 'B'
elif 70 <= average < 80:
    grade = 'C'
elif 60 <= average < 70:
    grade = 'D'
else:
    grade = 'F'

print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
