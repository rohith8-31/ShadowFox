# Task 1: Friends' names and lengths
print("Task 1 - Friends' Names and Lengths:")
friends = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
name_lengths = [(name, len(name)) for name in friends]
print("List of friends:", friends)
print("List of tuples (name, length):", name_lengths)
print()

# Task 2: Trip Expenses
print("Task 2 - Trip Expenses:")

# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate totals
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your expenses:", your_expenses)
print("Your total expenses:", your_total)
print("Partner's expenses:", partner_expenses)
print("Partner's total expenses:", partner_total)

# Who spent more
if your_total > partner_total:
    print("You spent more by:", your_total - partner_total)
else:
    print("Partner spent more by:", partner_total - your_total)

# Find category with significant difference
max_diff = 0
max_diff_category = ""
for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        max_diff_category = category

print("Category with biggest difference:", max_diff_category)
print("Difference in spending:", max_diff)