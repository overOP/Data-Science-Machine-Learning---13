# Exercise 1: Bug-Fixing (Float Precision & Mixed Division)
# Find and ﬁx the 2 bugs in this simple checkout calculator snippet so that it calculates the total with tax correctly and prints integer quantities safely.
# Goal: Calculate total price including tax, and display items per person
item_price = 12.50
quantity = int("4")
tax_rate = 0.08 # 8% tax

# Bug 1 occurs here when trying to calculate subtotal
subtotal = item_price * quantity
total_tax = subtotal * tax_rate
grand_total = subtotal + total_tax
num_people = 3

# Bug 2: We want cost_per_person to be an exact float, but items_per_person to be a whole number floor
cost_per_person = grand_total / num_people
items_per_person = quantity // num_people

print(f"Grand Total: ${grand_total}")
print(f"Items per person: {items_per_person}")