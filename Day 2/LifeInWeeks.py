# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until
# 90 years old.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days_90 = 365 * 90
weeks_90 = 52 * 90
months_90 = 12 * 90

int_age = int(age)

days_age = 365 * int_age
weeks_age = 52 * int_age
months_age = 12 * int_age

x_days = days_90 - days_age
y_weeks = weeks_90 - weeks_age
z_months = months_90 - months_age

print(f"You have {x_days} days, {y_weeks} weeks, and {z_months} months left.")