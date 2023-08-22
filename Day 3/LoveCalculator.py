# Write a program that tests the compatibility between two people.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()

# True
name1_t = lower_name1.count("t")
name1_r = lower_name1.count("r")
name1_u = lower_name1.count("u")
name1_e = lower_name1.count("e")

name2_t = lower_name2.count("t")
name2_r = lower_name2.count("r")
name2_u = lower_name2.count("u")
name2_e = lower_name2.count("e")

total_t = name1_t + name2_t
total_r = name1_r + name2_r
total_u = name1_u + name2_u
total_e = name1_e + name2_e
total_true = total_t + total_r + total_u + total_e

# Love
name1_l = lower_name1.count("l")
name1_o = lower_name1.count("o")
name1_v = lower_name1.count("v")
name1_e = lower_name1.count("e")

name2_l = lower_name2.count("l")
name2_o = lower_name2.count("o")
name2_v = lower_name2.count("v")
name2_e = lower_name2.count("e")

total_l = name1_l + name2_l
total_o = name1_o + name2_o
total_v = name1_v + name2_v
total_e = name1_e + name2_e
total_love = total_l + total_o + total_v + total_e

total_true_str = str(total_true)
total_love_str = str(total_love)

total_true_love = total_true_str + total_love_str
total_int = int(total_true_love)

if total_int < 10 or total_int > 90:
    print(f"Your score is {total_int}, you go together like coke and mentos.")
elif total_int >= 40 and total_int <= 50:
    print(f"Your score is {total_int}, you are alright together.")
else:
    print(f"Your score is {total_int}.")
