# 11. Write a function add(a, b) that returns the sum of two numbers.

# map ekti = function
# function define e def use hoy
def add(a,b):
    return a + b
# map string ke integer kore
a,b =map(int, input("Enter two numbers: ").split())
print(f"The sum is: {add(a, b)}")

# 12. Create a function is_palindrome(word) to check if a given string is a palindrome.  
def is_palindrome(r):
    return r ==r [:-1]
r = input('ENTER THE NUMBER:')
if is_palindrome(r):
    print(f"{r} is a palindrome.")
else:
    print(f"{r} is not a palindrome.")


# 13. Write a function factorial(n) to calculate the factorial of a number using a loop.  

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {factorial(n)}")

# 14. Create a function find_max(numbers) that returns the largest number in a list. 
def find_max(numbers):
    return max(numbers)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The largest number is: {find_max(numbers)}")


# 15. Write a function custom_power(base, exponent) that calculates base^exponent without using the **        operator or the pow() function.
def custom_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

base, exponent = map(int, input("Enter base and exponent: ").split())
print(f"{base} to the power of {exponent} is: {custom_power(base, exponent)}")
