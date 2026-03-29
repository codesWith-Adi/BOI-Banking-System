# 🏦 BOI Banking System (Python Mini Project)

A simple **console-based banking system** built using **Python**.  
This project is designed for **beginners** and demonstrates the use of:

- **Object-Oriented Programming (OOP)**
- **File Handling**
- **Basic User Authentication**
- **Transaction History Management**

---

## 📌 Project Overview

The **BOI Banking System** allows predefined users to:

- Login using their name
- Credit money into their account
- Debit money from their account
- Automatically save transaction history in a text file
- Maintain balance even after restarting the program

This project is made for **learning and practice purposes only**.

---

## 🚀 Features

- ✅ Predefined user database
- ✅ Credit amount
- ✅ Debit amount
- ✅ Insufficient balance handling
- ✅ Account number masking for privacy
- ✅ User-wise transaction history files
- ✅ Automatic balance recovery from saved file

---

## 🛠️ Technologies Used

- **Python 3**
- **datetime module**
- **File Handling**
- **Classes & Objects**

---

## 📂 Project Structure

```bash


BOI-Banking-System/
│
├── banking_system.py
├── README.md
├── .gitignore
├── sample_output.txt
│
└──Mini_Statement/
    ├── Aditya_9999.txt
    ├── Rohit_8888.txt
    └── ...
---


## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/codesWith-Adi/BOI-Banking-System.git
```

### 2. Open the project folder
```bash
cd BOI-Banking-System
```

### 3. Run the Python file
```bash
python banking_system.py
```

---

## 💻 Example Usage

```text
Enter your name: Aditya
What do you want to do? [c = credit / d = debit / e = exit]: c
Enter Amount to Credit: 500

You credited ₹500 in account no XXXXXX9999
Now your account has balance ₹500
```

---

## 📜 How It Works

### Step 1: User Login
The program asks for the user's name and checks it against a predefined users database.

### Step 2: File Creation
If the user logs in for the first time, a text file is automatically created to store their transaction history.

### Step 3: Load Previous Balance
The system reads the user's file and extracts the last saved balance.

### Step 4: Banking Operations
The user can choose:
- `c` → Credit money
- `d` → Debit money
- `e` → Exit program

### Step 5: Save Transaction
Every transaction is saved with:
- Amount
- Date and time
- Updated balance

---

## 🔐 Privacy Feature

To improve privacy, the account number is partially hidden.

Example:

```text
9999999999 → XXXXXX9999
```

---

## ⚠️ Limitations

This is a **beginner-level educational project**, so it does **not** include:

- Real password authentication
- Database integration
- GUI interface
- Encryption
- Real banking security

---

## 📈 Future Improvements

Possible upgrades for this project:

- Add **PIN / Password login**
- Add **Check balance option**
- Add **Transfer money feature**
- Add **Mini statement**
- Add **PDF Download**
- Add **GUI using Tkinter**
- Add **Database using MySQL / SQLite**
- Add **Admin panel**

-----------------------------------------------------------------------------------

## 👨‍💻 Author

**Aditya Kumar Pandey**  
**Diploma in CSE (1st Year Student)**  
Learning: Python, programming and Web development 🚀

-----------------------------------------------------------------------------------

## ⭐ If you like this project

Feel free to give a **star** on GitHub 🌟