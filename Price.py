# Get user input
price = float(input("Enter the price of the product: "))
discount_response = input("Enter the discount (yes or no): ")
# Function to apply 20% discount
def calculate_discount(price):
    return price * 0.8  # 80% of the price after applying a 20% discount

# Check if the user wants a discount
if discount_response == "yes":
    final_price = calculate_discount(price)  # Correct function call
    print(f"Final price after discount: Ksh {final_price:.2f}")
else:
    print(f"No discount applied. Final price: Ksh {price:.2f}")
