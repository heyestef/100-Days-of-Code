# Your first job is to build an automatic pizza order program.

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
size_price = 0

if size == "S":
    size_price += 15

elif size == "M":
    size_price += 20

else:
    size_price += 25

if add_pepperoni == "Y":
    if size == "S":
        size_price += 2
    else:
        size_price += 3

if extra_cheese == "Y":
    size_price += 1

print(f"Your final bill is: ${size_price}.")