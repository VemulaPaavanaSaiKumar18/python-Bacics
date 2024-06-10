# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.

# The last line of your program should print the result.

# Example 1 Input
# 39

# Example 1 Output
# 12
# Example 2 Input
# 43

# Example 2 Output
# 7

print("welcome to add 2 digits number")
num = int(input("Enter two digit number: "))

sum = 0            # Initializes the sum to 0.
while num > 0:     # Continues the loop as long as num is greater than 0.
		digit = num % 10      # Extracts the last digit of num using the modulus operator.
		sum += digit          # Adds the extracted digit to the sum.
		num //= 10            # Removes the last digit from num by performing integer division by 10.
print(sum)         # After the loop ends, prints the sum of the digits of the original num.