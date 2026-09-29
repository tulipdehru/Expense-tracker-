"""
Project 4: Expense Tracker
Syllabus used: List of Dictionaries, Set, Loops, Conditionals
"""

expenses = []  # list of dicts {"date":, "category":, "amount":}

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category-wise Total")
    print("4. Monthly Summary")
    print("5. Show Unique Categories")
    print("0. Exit")
    ch = input("Choice: ")

    if ch == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        expenses.append({"date": date, "category": category, "amount": amount})
        print("Expense added.")

    elif ch == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        for exp in expenses:
            print(exp)

    elif ch == "3":
        totals = {}  # category -> total amount
        for exp in expenses:
            cat = exp["category"]
            if cat in totals:
                totals[cat] = totals[cat] + exp["amount"]
            else:
                totals[cat] = exp["amount"]
        print("Category-wise Totals:")
        for cat in totals:
            print(cat, ":", totals[cat])

    elif ch == "4":
        month = input("Enter month-year to filter (MM-YYYY): ")
        total = 0
        for exp in expenses:
            date_parts = exp["date"].split("-")
            exp_month_year = date_parts[1] + "-" + date_parts[2]
            if exp_month_year == month:
                total = total + exp["amount"]
        print("Total expense for", month, ":", total)

    elif ch == "5":
        categories = set()
        for exp in expenses:
            categories.add(exp["category"])
        print("Unique Categories:", categories)

    elif ch == "0":
        print("Exiting Expense Tracker.")
        break
    else:
        print("Invalid choice.")
