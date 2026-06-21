# 🏦 FinVault Desktop Banking Suite

A modern desktop banking application built with Python and CustomTkinter that simulates real-world banking operations including account management, fund transfers, transaction tracking, passbook generation, and secure authentication.

Designed to demonstrate practical software engineering concepts such as Object-Oriented Programming, GUI Development, Authentication Systems, Data Persistence, and Financial Transaction Processing.

---

# 🌟 Key Highlights

✅ Secure PIN-Based Authentication

✅ Modern GUI using CustomTkinter

✅ Real-Time Balance Management

✅ Inter-Account Money Transfer

✅ Transaction History Tracking

✅ PDF Passbook Generation

✅ JSON-Based Persistent Storage

✅ Light & Dark Theme Support

✅ Account Number Privacy Masking

---

# 📸 Application Workflow

```text
User Login
     │
     ▼
Dashboard
     │
 ┌───┼──────────────┬───────────────┐
 ▼   ▼              ▼               ▼
Credit Debit     Transfer      History
 │      │            │              │
 ▼      ▼            ▼              ▼
Balance Updated → Transaction Recorded
                        │
                        ▼
                  PDF Passbook
```

---

# 🔐 Demo Accounts

Use any of the following accounts to test the application.

| Username    | PIN  |
| ----------- | ---- |
| Aditya      | 1234 |
| Rohit       | 2345 |
| Mohit       | 3456 |
| Ayush       | 4567 |
| Mohan       | 5678 |
| Prince      | 6789 |
| Raj         | 7890 |
| Anurag      | 8901 |
| Ashish      | 9012 |
| Priyadarshi | 0123 |

> These accounts are preloaded for demonstration and testing purposes.

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/codesWith-Adi/FinVault-Desktop-Banking-Suite.git
```

## Navigate to Project Folder

```bash
cd FinVault-Desktop-Banking-Suite
```

## Install Dependencies

```bash
pip install customtkinter reportlab
```

## Run Application

```bash
python main.py
```

---

# 🖥️ How to Login

### Step 1

Launch the application.

### Step 2

Enter a valid Username.

Example:

```text
Username: Aditya
```

### Step 3

Enter the corresponding PIN.

```text
PIN: 1234
```

### Step 4

Click Login.

Upon successful authentication, the Banking Dashboard will open.

---

# 📚 How to Use

## 💰 Credit Money

1. Click Credit.
2. Enter amount.
3. Confirm transaction.

Result:

* Balance increases.
* Transaction gets recorded.

---

## 💸 Debit Money

1. Click Debit.
2. Enter withdrawal amount.
3. Confirm transaction.

Result:

* Balance decreases.
* Insufficient balance is automatically handled.

---

## 🔄 Transfer Funds

1. Select Transfer.
2. Enter recipient username.
3. Enter amount.
4. Confirm transfer.

Result:

* Sender balance decreases.
* Receiver balance increases.
* Both histories are updated.

---

## 📜 View Transaction History

Click History to view:

* Credits
* Debits
* Transfers
* Received Payments
* Failed Transactions

with timestamps.

---

## 🔍 Search Transactions

Search records by date to quickly locate previous banking activity.

Example:

```text
07-04-2026
```

---

## 📄 Generate Passbook

Click Download Passbook.

A professional PDF statement will be generated containing:

* Account Holder Name
* Account Number
* Current Balance
* Complete Transaction History

---

## 🎨 Change Theme

Use the Theme Toggle option to switch between:

* Light Mode
* Dark Mode

---

# 🏗️ System Architecture

```text
GUI Layer (CustomTkinter)
            │
            ▼
Business Logic Layer
            │
            ▼
Banking Operations
(Credit / Debit / Transfer)
            │
            ▼
JSON Database
(users.json)
            │
            ▼
PDF Generator
(ReportLab)
```

---

# 🛠️ Technology Stack

| Technology    | Purpose                  |
| ------------- | ------------------------ |
| Python        | Core Development         |
| CustomTkinter | Modern GUI               |
| JSON          | Persistent Data Storage  |
| ReportLab     | PDF Generation           |
| Datetime      | Timestamp Management     |
| OOP           | Application Architecture |

---

# 📂 Project Structure

```text
FinVault-Desktop-Banking-Suite/
│
├── main.py
├── bank_logic.py
├── pdf_generator.py
├── users.json
│
├── assets/
│   └── images
│
├── PassBooks/
│   └── Generated PDF Statements
│
├── README.md
│
└── requirements.txt
```

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

* Object-Oriented Programming
* GUI Development
* Authentication Systems
* Financial Transaction Processing
* Data Persistence
* File Handling
* PDF Report Generation
* Modular Software Design

---

# 🔮 Future Enhancements

* SQLite/MySQL Integration
* User Registration Module
* Admin Dashboard
* OTP Authentication
* Email Notifications
* Interest Calculation
* Loan Management System
* Account Statement Export (Excel)
* Cloud Database Support
* Multi-Bank Architecture

---

# 👨‍💻 Developer

Aditya Kumar Pandey

Computer Science & Engineering Student

Focused on:

* Software Engineering
* Artificial Intelligence
* Full Stack Development
* Data Structures & Algorithms
* Open Source Development

---

# ⭐ Support

If you found this project useful:

⭐ Star the Repository

🍴 Fork the Project

🚀 Contribute New Features

💡 Share Feedback

---

### Built with Python ❤️

### Simulating Real Banking Operations Through Software Engineering 🚀
