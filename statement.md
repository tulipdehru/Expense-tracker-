# Problem Statement

Managing daily expenses manually can be difficult, especially when there are many expenses to keep track of. It can become hard to know how much money has been spent in different categories or during a particular month.
I wanted to make a simple Expense Tracker using Python that can be run directly on a computer. The project allows the user to add expenses with their date, category, and amount. It also allows the user to view all expenses, calculate category-wise totals, check monthly expenses, and display unique expense categories.

# Objectives

-To develop a simple expense tracking program using Python.
-To record expenses with date, category, and amount.
-To calculate the total expenses for different categories.
-To calculate the total expenses for a particular month.
-To display unique expense categories.
-To practice basic Python concepts such as lists, dictionaries, sets, loops, and conditional statements.

# Scope

This project focuses on providing a simple way to record and view personal expenses. It covers basic expense entry, expense display, category-wise calculation, monthly summary, and unique category identification.

The project is limited to temporary data storage while the program is running and does not include databases, online accounts, payment integration, or cloud storage.

# Target Users
Students who want to keep track of their daily expenses.
Beginners who want to practice basic Python programming concepts.
Users who need a simple way to calculate their monthly and category-wise expenses.

# High-Level Features
-Add Expense — The user can enter the date, category, and amount of an expense.
-View All Expenses — The user can view all expenses recorded during the current session.
-Category-wise Total — The program calculates the total amount spent in each category.
-Monthly Summary — The user can enter a month and year to find the total expenses for that month.
-Unique Categories — The program displays all unique expense categories using a set.
-Simple Menu — The user can select different operations through a menu-driven interface.

# Functional Requirements
1. Add Expense
2. View All Expenses
3. Category-wise Total
4. Monthly Summary
5. Show Unique Categories
6. Input and Error Handling

## Non-Functional Requirements
1. Usability,The program should have a simple menu so that users can easily understand and use its different options.
2. Performance, The program should process expenses quickly and display the results without noticeable delay.
3. Reliability, The program should correctly store expenses and calculate category-wise and monthly totals.
4. Maintainability, The code should be simple and organized so that it can be easily understood and modified.
5. Simplicity , The project should use basic Python concepts and remain suitable for beginners.

## System Architecture

The application follows a simple console-based architecture.

- User Interface: The program uses the Python console to display the menu and take input from the user.
- Expense Data: Expenses are stored in a list of dictionaries containing the date, category, and amount.
- Processing: Loops and conditional statements are used to process expenses and perform calculations.
- Category Management: A set is used to identify unique categories.
- Results: The calculated totals and expense information are displayed in the console.

## Process Flow
1. The program starts and displays the Expense Tracker menu.
2. The user selects an option from the menu.
3. If the user selects Add Expense, the date, category, and amount are entered.
4. The expense is stored in the list of dictionaries.
5. The user can view all recorded expenses.
6. The program can calculate category-wise totals.
7. The user can enter a month and year to calculate the monthly total.
8. The program can display unique categories using a set.
9. The user can continue using different options.
10.  The program exits when the user selects the Exit option.