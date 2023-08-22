# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

int_w = int(weight)
flt_h = float(height)

bmi = int_w / (flt_h ** 2)
print(int(bmi))
