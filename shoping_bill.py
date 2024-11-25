from random import choice

# Initialize with an empty list to store products
products = []

def generate_product_code():
    """Generates a unique 6-character product code."""
    code_nums = list(range(0, 10)) + ["B", "C", "E", "F"]
    code = ''.join(str(choice(code_nums)) for _ in range(6))
    return code

def get_valid_price():
    """Prompts the user for a valid price input."""
    while True:
        try:
            price = float(input("Enter product price: "))
            if price <= 0:
                print("Price must be greater than 0. Please try again.")
                continue
            return price
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")

def calculate_discount(total):
    """Calculates the discount based on the total amount."""
    if 60 < total <= 90:
        discount_rate = 0.10
    elif 90 < total <= 140:
        discount_rate = 0.15
    elif 140 < total <= 1200:
        discount_rate = 0.20
    elif total > 1200:
        discount_rate = 0.07
    else:
        discount_rate = 0.0  # No discount for totals <= 60
    discount = total * discount_rate
    return total - discount, discount, discount_rate * 100

# Active flag for open counter
counter_open = True
while counter_open:
    # Scan Product
    product_name = input("Enter product name: ").strip()
    product_price = get_valid_price()
    product_code = generate_product_code()

    # Append product details in products list
    products.append((product_name, product_price, product_code))

    # Ask user if they want to scan more products
    exit_ask = input("Do you want to scan more products? (yes/no): ").strip().lower()
    if exit_ask == 'no':
        counter_open = False

# Mart Heading
print("\n----- BIG BUY -----")
print(f"{'Product Name':<20} {'Code':<10} {'Price':>10}")
print("-" * 40)

# Show product details
total = 0
for name, price, code in products:
    print(f"{name:<20} {code:<10} ${price:>10.2f}")
    total += price

# Total Heading
print("\n----- Total Bill -----")
print(f"Subtotal: ${total:.2f}")

# Apply discount
final_total, discount, discount_rate = calculate_discount(total)
if discount > 0:
    print(f"Discount ({discount_rate:.0f}%): -${discount:.2f}")
else:
    print("No discount applied.")

# Apply tax
tax_rate = 0.05
tax = final_total * tax_rate
final_total += tax
print(f"Tax (5%): +${tax:.2f}")

# Final amount
print(f"Final Amount: ${final_total:.2f}")
print("-" * 40)
print("Thank you for shopping at BIG BUY!")
