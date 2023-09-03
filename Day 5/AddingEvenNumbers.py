# Write a program that calculates the sum of all the even numbers from 1 to 100

# Write your code below this row 👇

sum_even = 0
for number in range(2,101,2):
    sum_even += number

print(sum_even)