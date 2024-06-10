import sys
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

# Example Input
# L
# Y
# N
# Example Output
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.

print("welcome to pizza deliveries")

size = input("what size pizza do you want? \n Small pizza (S): $15 enter S \n Medium pizza (M): $20 enter M\n Large pizza (L): $25 enter L\n Enter your choice: ")

bill = 0
order = ""

if size == "S":
	bill += 15
	order += "small pizza"
elif size == "M":
	bill += 20
	order += "medium pizza"
elif size == "L":
	bill += 25
	order += "large pizza"
else:
	print("invalid input for size of pizza try again please enter S, M or L in caps")
	sys.exit()

add_pepperoni_small = input("Add pepperoni for small pizza (Y or N):")
add_pepperoni_medium = input("Add pepperoni for medium (Y or N):")
add_pepperoni_large = input("Add pepperoni for large pizza (Y or N):")
extra_cheese = input("Add extra cheese for any size pizza (Y or N):")

if add_pepperoni_small == "Y":
		bill += 2
		order += " \n one pepperoni of small pizza"
if add_pepperoni_medium == "Y":
		bill += 3
		order += " \n one pepperoni of medium pizza"
if add_pepperoni_large == "Y":
		bill += 3
		order += " \n one pepperoni of large pizza"
if add_pepperoni_small == "N" and add_pepperoni_medium == "N" and add_pepperoni_large == "N":
		order += " \n without pepperoni"
if extra_cheese == "Y":
		bill += 1
		order += " and with extra cheese"
if extra_cheese == "N":
		order += " and without extra cheese"

print(f"your order is: {order}")
print(f"your final bill is: ${bill}")
print("Thank you for choosing Pizza Deliveries!")