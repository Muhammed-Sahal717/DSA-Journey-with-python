"""Task: Simple Shopping Cart Analyzer
Problem Statement

Write a Python program that does the following:

Create a list of item prices (at least 6 items).

Use a loop to:

Display each item price

Calculate the total bill amount

Use if / elif / else to apply discount rules:

If total ≥ 2000 → 20% discount

If total ≥ 1500 → 10% discount

If total ≥ 1000 → 5% discount

Else → No discount

Calculate and print:

Discount amount

Final payable amount

Find and print:

Highest priced item

Lowest priced item

⚙️ Rules

Use only one list

Use at least one loop

Use if / elif / else

Do not use functions yet"""

# Step 1: List of item pricesitem_prices = [250, 450, 300, 700, 150, 600]
item_prices = [250, 450, 300, 700, 150, 600]
# Step 2: Initialize total bill amount
total_bill = 0
# Step 3: Loop through the list to display prices and calculate total
print("Item Prices:")
for price in item_prices:
    print(f"- ${price}")
    total_bill += price
# Step 4: Apply discount rules
if total_bill >= 2000:
    discount_rate = 0.20
elif total_bill >= 1500:
    discount_rate = 0.10
elif total_bill >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.0
discount_amount = total_bill * discount_rate
final_amount = total_bill - discount_amount
# Step 5: Find highest and lowest priced items
highest_price = max(item_prices)
lowest_price = min(item_prices)
# Step 6: Print results
print(f"\nTotal Bill Amount: ${total_bill:.2f}")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Final Payable Amount: ${final_amount:.2f}")
print(f"Highest Priced Item: ${highest_price}")
print(f"Lowest Priced Item: ${lowest_price}")
