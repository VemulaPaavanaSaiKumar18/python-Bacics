from assets import MENU, resources
def report(resources):
	print(f"Water: {resources['water']}ml")
	print(f"Milk: {resources['milk']}ml")
	print(f"Coffee: {resources['coffee']}g")
	print(f"Money: ${resources['money']}")


def is_resource_sufficient(order_ingredients):
	for item in order_ingredients:
		if order_ingredients[item] >= resources[item]:
			print(f"Sorry there is not enough {item}")
			return False
	return True

def transaction_successful(money_received, drink_cost):
		if money_received >= drink_cost:
				change = round(money_received - drink_cost, 2)
				print(f"Here is ${change} in change.")
				resources["money"] += drink_cost
				return True
		else:
				print("Sorry that's not enough money. Money refunded.")
				return False
		
def make_coffee(drink_name, order_ingredients):
	for item in order_ingredients:
		resources[item] -= order_ingredients[item]
	print(f"Here is your {drink_name} ☕. Enjoy!")

def calculate_money(quarters, dimes, nickles, pennies):
	return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)


profit = 0
is_on = True

while is_on:
	options = input("What would you like? (espresso/latte/cappuccino): ")
	if options == "off":
		is_on = False
	elif options == "report":
		report(resources)
	else:
		drink = MENU[options]
		quarters = float(input("How many quarters?: "))
		dimes = float(input("How many dimes?: "))
		nickles = float(input("How many nickles?: "))
		pennies = float(input("How many pennies?: "))
		if is_resource_sufficient(drink["ingredients"]):
			transaction = transaction_successful(calculate_money(quarters, dimes, nickles, pennies), drink["cost"])
			if transaction:
				make_coffee(options, drink["ingredients"])
