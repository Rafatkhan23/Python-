
# 1. Write a program to check if a number is even or odd using an if-else statement.

number =int (input("inter your namber"))
if number / 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# 2. Write a program to check if a number is positive, negative, or zero. 
 

number =int(input("Inter your namber"))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")

# 3. Create a program to determine the grade of a student based on their marks:
#    - 90 and above: A  
#    - 80–89: B  
#    - 70–79: C  
#    - Below 70: Fail  
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")

# 4. Write a program that checks if a given year is a leap year.  

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")


# # 5. Take three numbers as input and find the largest of them using if-else.  
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >= b and a >= c:
    print(f"The largest number is {a}.")
elif b >= a and b >= c:
    print(f"The largest number is {b}.")
else:
    print(f"The largest number is {c}.")

