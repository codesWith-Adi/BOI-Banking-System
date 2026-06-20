import json
from datetime import datetime

FILE_NAME = "users.json"


def load_users():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)


class BOI:
    def __init__(self, name, account_no, pin, balance, history):
        self.name = name
        self.account_no = account_no
        self.pin = pin
        self.balance = balance
        self.history = history if isinstance(history, list) else []

    @property
    def hide_acc(self):
        return "X" * 6 + self.account_no[6:]

    def credit(self, amount):
        self.balance += amount
        dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        transaction = f"{dt}|CREDIT|₹{amount}|₹{self.balance}"
        self.history.append(transaction)
        return f"Credited ₹{amount} successfully"

    def debit(self, amount):
        dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        if amount > self.balance:
            transaction = f"{dt}|FAILED DEBIT|₹{amount}|₹{self.balance}"
            self.history.append(transaction)
            return False, f"Insufficient balance! Available balance: ₹{self.balance}"

        self.balance -= amount
        transaction = f"{dt}|DEBIT|₹{amount}|₹{self.balance}"
        self.history.append(transaction)
        return True, f"Debited ₹{amount} successfully"

    def transfer(self, amount, receiver_name):
        dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        if amount > self.balance:
            self.history.append(f"{dt}|FAILED TRANSFER to {receiver_name}|₹{amount}|₹{self.balance}")
            return False, f"Insufficient balance! Available balance: ₹{self.balance}"

        self.balance -= amount
        self.history.append(f"{dt}|TRANSFER to {receiver_name}|₹{amount}|₹{self.balance}")
        return True, f"Transferred ₹{amount} to {receiver_name}"

    def receive_transfer(self, amount, sender_name):
        dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.balance += amount
        self.history.append(f"{dt}|RECEIVED from {sender_name}|₹{amount}|₹{self.balance}")

    def to_dict(self):
        return {
            "account_no": self.account_no,
            "pin": self.pin,
            "balance": self.balance,
            "history": self.history
        }


def get_user(username, pin):
    users = load_users()

    for user in users:
        if user.lower() == username.lower():
            if users[user]["pin"] == pin:
                data = users[user]
                return user, BOI(
                    user,
                    data["account_no"],
                    data["pin"],
                    data["balance"],
                    data.get("history", [])
                )
            else:
                return None, None

    return None, None


def get_user_by_name(username):
    users = load_users()

    for user in users:
        if user.lower() == username.lower():
            data = users[user]
            return user, BOI(
                user,
                data["account_no"],
                data["pin"],
                data["balance"],
                data.get("history", [])
            )

    return None, None


def update_user(user_obj):
    users = load_users()

    # only update the current user, keep all others untouched
    if user_obj.name in users:
        users[user_obj.name]["account_no"] = user_obj.account_no
        users[user_obj.name]["pin"] = user_obj.pin
        users[user_obj.name]["balance"] = user_obj.balance
        users[user_obj.name]["history"] = user_obj.history
    else:
        users[user_obj.name] = user_obj.to_dict()

    save_users(users)