# Write a program that will select a random name from a list of names

# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# print(names)
# Write your code below this line 👇

len_list = len(names)
name_random = random.randint(0, len_list)
name = names[name_random]
print(f'{name} is going to buy the meal today!')