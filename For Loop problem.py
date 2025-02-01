# 6. Write a program to print all even numbers from 1 to 50 using a for loop. 
for num in range(1, 50):
 if num % 2==0:
    print(num, end=" ")
    print("\n")


    # \n line bfreak er kaj kore

# 7. Create a program that calculates the sum of the first 10 natural numbers using a for loop.  
sum_of_numbers = 0

for num in range(1, 11):
    sum_of_numbers += num

print(f"The sum of the first 10 natural numbers is:{sum_of_numbers}")
print("\n")

# 8. Write a program to display the multiplication table of a number input by the user.  
number = int(input("Enter a number:"))
for i in range(1, 10):
    print(f"{number} x {i} = {number * i}")

# 9. Write a program that prints all prime numbers between 1 and 100.  
for num in range(1, 100):
    is_prime = True
    # num**0.5=rut er kaj kore
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        print("\n")

# 10. Write a program that generates the first n Fibonacci numbers and checks if a given number is part of the sequence.
num = int(input("How many Fibonacci numbers? "))
n1=0
n2=1
sum=0
if num<=0:
    print("fu")
else:
    for i in range(0,num):
        print(sum,end="")
        n1=n2
        n2=sum
        sum=n1+n2
