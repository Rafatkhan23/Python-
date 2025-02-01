# 16. Write a program to calculate the average of numbers in a list.
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"The average is: {average}")
else:
    print("No numbers entered.")

# 17. Create a program to find the second largest number in a list.
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
second_largest = sorted(set(numbers))[-2]
print(f"The second largest number is: {second_largest}")

# 18. Write a program that takes an input in minutes and converts it to hours and minutes.
# Example: 130 minutes → 2 hours and 10 minutes.
minutes = 130
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} minutes is {hours} hours and {remaining_minutes} minutes.")

# 19. Given a list of integers, write a program to count how many of them are positive, negative, and zero.
numbers = [12, 23, 45, 89]
positive = sum(1 for num in numbers if num > 0)
negative = sum(1 for num in numbers if num < 0)
zeros = numbers.count(0)
print(f"Positive: {positive}, Negative: {negative}, Zero: {zeros}")

# 20. Write a program to find the sum of all odd numbers in a list.
numbers = list(map(int, input("Enter the numbers: ").split()))
sum_of_odds = sum(num for num in numbers if num % 2 != 0)
print(f"সব বিজোড় সংখ্যার যোগফল হলো: {sum_of_odds}")