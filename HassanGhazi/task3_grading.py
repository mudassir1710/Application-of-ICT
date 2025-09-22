marks = int(input("Enter your marks:"))

grade = "h"
if marks >=90 and marks <=100:
    grade = "A"
    print("Grade: ", grade)
elif marks >=75 and marks <90:
    grade = "B"
    print("Grade: ", grade)
elif marks >=50 and marks <75:
    grade = "C"
    print("Grade: ", grade)
elif marks >0 and marks <50:
    grade = "F"
    print("Grade: ", grade)
else: 
    
    print("Invalid")
