"""
Project Title: BOI Banking System

Author: Aditya Kumar Pandey
Course: Diploma in Computer Science (1st Year)

Description:
    This is a beginner-friendly console-based banking system built using Python.
    It includes:
    - Object-Oriented Programming (OOP)
    - File Handling
    - User Authentication (basic name check)
    - Credit / Debit operations
    - Transaction History Storage

Note:
    - This project is made for learning purposes only.
    - It is not a real banking application and does not include real security features.

    ------------------------------------------------------------------------------------------

    - This projeject is under development, it will be updated with more features in the future.

    ------------------------------------------------------------------------------------------
"""

from datetime import datetime


class BOI:
    """
    BOI class represents a bank account user.
    
    Attributes:
        name (str): Name of the account holder
        balance (int): Current balance of the account
        account_no (str): Account number of the user
        hide_acc (str): Masked account number for display
    """

    def __init__(self, name, balance, acc):
        self.name = name
        self.balance = balance
        self.account_no = acc

        # Masking account number for privacy
        # Example: 9999999999 -> XXXXXX9999
        self.hide_acc = "X" * 6 + self.account_no[6:]

    def credit(self, amount):
        """
        Adds money to the user's account.

        Args:
            amount (int): Amount to credit

        Returns:
            str: Transaction history string to save in file
        """
        self.balance += amount
        print(
            f"You credited ₹{amount} in account no {self.hide_acc}\n"
            f"Now your account has balance ₹{self.balance}\n"
        )
        return (
            f"Credited amount ₹{amount} at {datetime.now()}\n"
            f"Main balance:\n{self.balance}\n\n"
        )

    def debit(self, amount):
        """
        Deducts money from the user's account if sufficient balance exists.

        Args:
            amount (int): Amount to debit

        Returns:
            str: Transaction history string to save in file
        """
        if amount > self.balance:
            print("Insufficient balance\n")
            return (
                f"Failed to debit amount ₹{amount} at {datetime.now()}\n"
                f"Main balance:\n{self.balance}\n\n"
            )

        self.balance -= amount
        print(
            f"You debited amount ₹{amount} from account no {self.hide_acc}\n"
            f"Now your account has balance ₹{self.balance}\n"
        )
        return (
            f"Debited amount ₹{amount} at {datetime.now()}\n"
            f"Main balance:\n{self.balance}\n\n"
        )


# -------------------------------
# USERS DATABASE
# -------------------------------
# Dictionary storing usernames and their account numbers
users = {
    "Aditya": "9999999999",
    "Rohit": "8888888888",
    "Mohit": "7777777777",
    "Ayush": "6666666666",
    "Mohan": "5555555555",
    "Prince": "4444444444",
    "Raj": "3333333333",
    "Anurag": "2222222222",
    "Ashish": "1111111111",
    "Priyadarshi": "0000000000"
}


# -------------------------------
# MAIN PROGRAM LOOP
# -------------------------------
while True:
    username = input("Enter your name: ")

    # Check username case-insensitively
    if username.lower() in [user.lower() for user in users]:

        # Fix the username case to match dictionary key
        for user in users:
            if username.lower() == user.lower():
                username = user
                break

        # Create unique file name for each user
        filename = (f"Mini_Statement/{username}_{users[username][6:]}.txt")  # Example: Aditya_9999.txt
        # Create file if it does not exist
        with open(filename, "a", encoding="utf-8") as f:
            pass

        # Read previous transaction history
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # -------------------------------
        # LOAD LAST BALANCE SAFELY
        # -------------------------------
        if lines == []:
            last_balance = 0
        else:
            last_balance = 0
            for line in reversed(lines):
                if line.strip().isdigit():
                    last_balance = int(line.strip())
                    break

        # Create user account object
        User = BOI(username, last_balance, users[username])

        # If file is empty, write header
        if lines == []:
            with open(filename, "a", encoding="utf-8") as f:
                f.write(
                    f"UserName: {User.name}\n"
                    f"Account no.: {User.account_no}\n\n"
                    f"History:\n"
                )

        # Ask user what operation they want
        work = input("What do you want to do? [c = credit / d = debit / e = exit]: ")

        if work == "c":
            try:
                cr = int(input("Enter Amount to Credit: "))
                if cr <= 0:
                    print("Invalid amount\n")
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(User.credit(cr))
            except ValueError:
                print("Invalid amount\n")

        elif work == "d":
            try:
                db = int(input("Enter Amount to Debit: "))
                if db <= 0:
                    print("Invalid amount\n")
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(User.debit(db))
            except ValueError:
                print("Invalid amount\n")

        elif work == "e":
            print("Thank you for using BOI Banking System")
            break

        else:
            print("Invalid input\n")

    else:
        print("User not found in BOI database\n")