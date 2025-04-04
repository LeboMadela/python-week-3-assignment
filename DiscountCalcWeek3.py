#Author: Moleboheng Madela
#Date: 2025-04-04
#Description: Create a function that returns discounted price of an item.
#The function should take two parameters: price and disc_percent.

# This function calculates the price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

# Ask the user for the original price and discount percent
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Use the function to get the final price
final_price = calculate_discount(price, discount_percent)

# Show the result
if discount_percent >= 20:
    print("Discount applied!")
else:
    print("No discount applied.")

print("Final price: R", round(final_price, 2))
