print("Expense split calculator:")
spent = float(input("Enter your total spent amount: "))
tip = float(input("Enter your tip amount, ex: 10, 20, and 30: "))
total_amount = spent + (1+ tip/100)
split_count = int(input("Enter the total of numbers to split: "))

split_amount = round(total_amount / split_count, 2)

print(f"The split amount is: {split_amount}")