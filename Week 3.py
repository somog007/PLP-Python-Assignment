def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage to apply
    
    Returns:
    float: Final price after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percentage)

# Display the result
if discount_percentage >= 20:
    print(f"After applying a {discount_percentage}% discount, the final price is: ₦{final_price:.2f}")
else:
    print(f"No discount applied (needs to be 20% or higher). The price remains: ₦{original_price:.2f}")
