A simple Python program that checks marks and displays the grade and Pass/Fail result.

# Take marks from the user
marks = int(input("Enter your marks (0-100): "))

# Check the marks
if marks >= 80:
    print("Grade: A")
    print("Result: Pass")

elif marks >= 70:
    print("Grade: B")
    print("Result: Pass")

elif marks >= 60:
    print("Grade: C")
    print("Result: Pass")

elif marks >= 50:
    print("Grade: D")
    print("Result: Pass")

else:
    print("Grade: F")
    print("Result: Fail")
