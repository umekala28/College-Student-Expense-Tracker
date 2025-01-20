print("Script started successfully!")
import csv
import os

# File name for saving data
FILE_NAME = "college_student_expense_tracker.csv"

# Initialize budgeting category structures
income_data = []
fixed_expenses = []
variable_expenses = []
budget_data = {}

# Predefined categories + customization
INCOME_CATEGORIES = [
    "Parental Support",
    "Student Loans",
    "On-Campus Job",
    "Internship",
    "Scholarships/Grants",
    "Other"
]

VARIABLE_EXPENSE_CATEGORIES = [
    "Dining Out",
    "Entertainment",
    "Transportation",
    "Other"
]

# User-specific data
semester_name = ""
on_campus = False
monthly_housing = 0.0
monthly_dining = 0.0
monthly_subscriptions = 0.0
credit_card_payment = 0.0
savings_goal = 0.0


# Load existing data from CSV
def load_data():
    global income_data, fixed_expenses, variable_expenses
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                category, amount, entry_type = row
                if entry_type == "income":
                    income_data.append({"category": category, "amount": float(amount)})
                elif entry_type == "fixed":
                    fixed_expenses.append({"category": category, "amount": float(amount)})
                elif entry_type == "variable":
                    variable_expenses.append({"category": category, "amount": float(amount)})


# Save data to CSV
def save_data():
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Amount", "Type"])
        for entry in income_data:
            writer.writerow([entry["category"], entry["amount"], "income"])
        for entry in fixed_expenses:
            writer.writerow([entry["category"], entry["amount"], "fixed"])
        for entry in variable_expenses:
            writer.writerow([entry["category"], entry["amount"], "variable"])
    print("Data saved successfully!")


# Add income in all categories 
def add_income():
    print("\n=== Add Income ===")
    print("Choose an income source:")
    for i, category in enumerate(INCOME_CATEGORIES, start=1):
        print(f"{i}. {category}")
    choice = int(input("Enter the number of your choice: "))
    if 1 <= choice <= len(INCOME_CATEGORIES):
        category = INCOME_CATEGORIES[choice - 1]
        if category == "Other":
            category = input("Enter the custom income source: ")
        amount = float(input("Enter amount: "))
        income_data.append({"category": category, "amount": amount})
        print(f"Income added: {category} - ${amount:.2f}")
    else:
        print("Invalid choice. Returning to main menu.")


# Add variable expenses
def add_variable_expense():
    print("\n=== Add Variable Expense ===")
    print("Choose an expense category:")
    for i, category in enumerate(VARIABLE_EXPENSE_CATEGORIES, start=1):
        print(f"{i}. {category}")
    choice = int(input("Enter the number of your choice: "))
    if 1 <= choice <= len(VARIABLE_EXPENSE_CATEGORIES):
        category = VARIABLE_EXPENSE_CATEGORIES[choice - 1]
        if category == "Other":
            category = input("Enter the custom expense category: ")
        amount = float(input("Enter amount: "))
        variable_expenses.append({"category": category, "amount": amount})
        print(f"Expense added: {category} - ${amount:.2f}")
    else:
        print("Invalid choice. Returning to main menu.")


# Set up personal monthly budget
def setup_budget():
    global monthly_housing, monthly_dining, monthly_subscriptions, credit_card_payment, savings_goal

    print("\n=== Monthly Budget Setup ===")
    monthly_housing = float(input("Enter your monthly housing cost: "))
    monthly_dining = float(input("Enter your monthly dining/groceries cost: "))
    monthly_subscriptions = float(input("Enter your total monthly subscription cost (e.g., Netflix, Spotify): "))
    credit_card_payment = float(input("Enter your monthly credit card payment: "))
    savings_goal = float(input("Enter your monthly savings goal: "))

    # Add fixed expenses to the list
    fixed_expenses.append({"category": "Housing", "amount": monthly_housing})
    fixed_expenses.append({"category": "Dining/Groceries", "amount": monthly_dining})
    fixed_expenses.append({"category": "Subscriptions", "amount": monthly_subscriptions})
    fixed_expenses.append({"category": "Credit Card Payment", "amount": credit_card_payment})
    fixed_expenses.append({"category": "Savings Goal", "amount": savings_goal})

    print("\nBudget setup complete!")


# View personal finance summary
def view_summary():
    total_income = sum(entry["amount"] for entry in income_data)
    total_fixed_expenses = sum(entry["amount"] for entry in fixed_expenses)
    total_variable_expenses = sum(entry["amount"] for entry in variable_expenses)
    remaining_budget = total_income - (total_fixed_expenses + total_variable_expenses)

    print("\n===== Monthly Summary =====")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Fixed Expenses: ${total_fixed_expenses:.2f}")
    print(f"Variable Expenses: ${total_variable_expenses:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")
    print("===========================\n")


# Main menu
def main_menu():
    load_data()
    setup_budget()
    while True:
        print("\n=== College Expense Tracker ===")
        print("1. Add Income")
        print("2. Add Variable Expense")
        print("3. View Summary")
        print("4. Save & Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_variable_expense()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
if __name__ == "__main__":
    main_menu()