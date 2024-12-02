def calculate_tip(total_bill, tip_percentage):
    # Calculate the tip amount
    tip = (tip_percentage / 100) * total_bill
    return tip

def calculate_total_amount(total_bill, tip):
    # Calculate the total amount (bill + tip)
    total_amount = total_bill + tip
    return total_amount

# Input from user
total_bill = float(input("Enter the total bill amount: $"))
tip_percentage = float(input("Enter the tip percentage (e.g., 15, 20): "))
people = int(input("Enter total people:"))

# Calculate tip and total amount
tip = calculate_tip(total_bill, tip_percentage)
total_amount = calculate_total_amount(total_bill, tip)
split_bill = total_amount/people

# Output results
print(f"Tip: ${tip:.2f}")
print(f"Total amount (bill + tip): ${total_amount:.2f}")
print(f"Total bill for each individual:{split_bill}")