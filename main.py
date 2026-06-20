import customtkinter as ctk
from tkinter import messagebox
from bank_logic import get_user, update_user, get_user_by_name
from pdf_generator import generate_passbook_pdf

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BOI Banking System")
        self.root.geometry("1200x750")
        self.root.state("zoomed")

        self.current_user = None
        self.theme_mode = "dark"

        self.create_login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def toggle_theme(self):
        if(self.theme_mode == "dark"):
            self.theme_mode = "light"
            ctk.set_appearance_mode("light")
        else:
            self.theme_mode = "dark"
            ctk.set_appearance_mode("dark")

        if(self.current_user):
            self.create_dashboard()
        else:
            self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()

        main_frame = ctk.CTkFrame(self.root, corner_radius=20)
        main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.35, relheight=0.6)

        title = ctk.CTkLabel(main_frame, text="🏦 BOI Banking Login", font=("Segoe UI", 28, "bold"))
        title.pack(pady=30)

        self.username_entry = ctk.CTkEntry(main_frame, placeholder_text="Enter Username", width=300, height=45)
        self.username_entry.pack(pady=15)

        self.pin_entry = ctk.CTkEntry(main_frame, placeholder_text="Enter PIN", width=300, height=45, show="*")
        self.pin_entry.pack(pady=15)

        login_btn = ctk.CTkButton(main_frame, text="Login", width=220, height=45, command=self.login_user)
        login_btn.pack(pady=20)

        theme_btn = ctk.CTkButton(main_frame, text="🌙 / ☀ Toggle Theme", width=220, height=40, command=self.toggle_theme)
        theme_btn.pack(pady=10)

    def login_user(self):
        username = self.username_entry.get().strip()
        pin = self.pin_entry.get().strip()

        actual_name, user = get_user(username, pin)

        if(user is None):
            messagebox.showerror("Login Failed", "Invalid Username or PIN")
        else:
            self.current_user = user
            self.create_dashboard()

    def create_dashboard(self):
        self.clear_screen()

        top_frame = ctk.CTkFrame(self.root, height=80, corner_radius=0)
        top_frame.pack(fill="x")

        welcome_label = ctk.CTkLabel(top_frame, text=f"Welcome, {self.current_user.name}", font=("Segoe UI", 28, "bold"))
        welcome_label.pack(side="left", padx=30, pady=20)

        theme_btn = ctk.CTkButton(top_frame, text="🌙 / ☀ Theme", width=120, command=self.toggle_theme)
        theme_btn.pack(side="right", padx=20, pady=20)

        logout_btn = ctk.CTkButton(top_frame, text="Logout", width=120, fg_color="red", command=self.logout)
        logout_btn.pack(side="right", padx=10, pady=20)

        main_frame = ctk.CTkFrame(self.root, corner_radius=20)
        main_frame.pack(pady=30, padx=40, fill="both", expand=True)

        account_label = ctk.CTkLabel(main_frame, text=f"Account No: {self.current_user.hide_acc}", font=("Segoe UI", 18))
        account_label.pack(pady=10)

        self.balance_label = ctk.CTkLabel(main_frame, text=f"₹ {self.current_user.balance}", font=("Segoe UI", 36, "bold"))
        self.balance_label.pack(pady=15)

        self.amount_entry = ctk.CTkEntry(main_frame, placeholder_text="Enter Amount", width=250, height=45)
        self.amount_entry.pack(pady=10)

        btn_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        btn_frame.pack(pady=20)

        ctk.CTkButton(btn_frame, text="➕ Credit", width=140, command=self.credit_amount).grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkButton(btn_frame, text="➖ Debit", width=140, fg_color="red", command=self.debit_amount).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(btn_frame, text="💸 Transfer", width=140, fg_color="orange", command=self.open_transfer_window).grid(row=0, column=2, padx=10, pady=10)
        ctk.CTkButton(btn_frame, text="📜 History", width=140, fg_color="purple", command=self.show_history).grid(row=0, column=3, padx=10, pady=10)

        search_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        search_frame.pack(pady=10)

        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search by date (dd-mm-yyyy)", width=220, height=40)
        self.search_entry.grid(row=0, column=0, padx=10)

        ctk.CTkButton(search_frame, text="🔍 Search", width=120, command=self.search_history).grid(row=0, column=1, padx=10)

        ctk.CTkButton(main_frame, text="📄 Download PDF Passbook", width=250, height=45, fg_color="green", command=self.download_pdf).pack(pady=20)

    def credit_amount(self):
        try:
            amount = int(self.amount_entry.get())
            if amount <= 0:
                raise ValueError

            message = self.current_user.credit(amount)
            update_user(self.current_user)
            self.balance_label.configure(text=f"₹ {self.current_user.balance}")
            self.amount_entry.delete(0, "end")
            messagebox.showinfo("Success", message)

        except ValueError:
            messagebox.showerror("Error", "Enter a valid positive amount")

    def debit_amount(self):
        try:
            amount = int(self.amount_entry.get())
            if amount <= 0:
                raise ValueError

            success, message = self.current_user.debit(amount)
            update_user(self.current_user)
            self.balance_label.configure(text=f"₹ {self.current_user.balance}")
            self.amount_entry.delete(0, "end")

            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Failed", message)

        except ValueError:
            messagebox.showerror("Error", "Enter a valid positive amount")

    def open_transfer_window(self):
        transfer_window = ctk.CTkToplevel(self.root)
        transfer_window.title("Transfer Money")
        transfer_window.geometry("400x300")

        ctk.CTkLabel(transfer_window, text="💸 Transfer Money", font=("Segoe UI", 24, "bold")).pack(pady=20)

        receiver_entry = ctk.CTkEntry(transfer_window, placeholder_text="Receiver Username", width=250, height=40)
        receiver_entry.pack(pady=10)

        amount_entry = ctk.CTkEntry(transfer_window, placeholder_text="Amount", width=250, height=40)
        amount_entry.pack(pady=10)

        def transfer_now():
            receiver_name = receiver_entry.get().strip()

            try:
                amount = int(amount_entry.get())
                if amount <= 0:
                    raise ValueError

                actual_name, receiver = get_user_by_name(receiver_name)

                if receiver is None:
                    messagebox.showerror("Error", "Receiver not found")
                    return

                if receiver.name == self.current_user.name:
                    messagebox.showerror("Error", "You cannot transfer money to yourself")
                    return

                success, msg = self.current_user.transfer(amount, receiver.name)

                if success:
                    receiver.receive_transfer(amount, self.current_user.name)
                    update_user(self.current_user)
                    update_user(receiver)
                    self.balance_label.configure(text=f"₹ {self.current_user.balance}")
                    messagebox.showinfo("Success", msg)
                    transfer_window.destroy()
                else:
                    messagebox.showerror("Failed", msg)

            except ValueError:
                messagebox.showerror("Error", "Enter a valid amount")

        ctk.CTkButton(transfer_window, text="Transfer", width=180, command=transfer_now).pack(pady=20)

    def show_history(self, filtered_history=None):
        history_window = ctk.CTkToplevel(self.root)
        history_window.title("Bank Passbook")
        history_window.geometry("950x550")

        ctk.CTkLabel(history_window, text="🏦 BOI DIGITAL PASSBOOK", font=("Segoe UI", 24, "bold")).pack(pady=20)

        history_box = ctk.CTkTextbox(history_window, width=900, height=430, font=("Consolas", 14))
        history_box.pack(pady=10)

        history_box.insert("end", "=" * 90 + "\n")
        history_box.insert("end", f"{'DATE & TIME':<22}{'TYPE':<28}{'AMOUNT':<18}{'AVAILABLE BALANCE':<20}\n")
        history_box.insert("end", "=" * 90 + "\n")

        history_data = filtered_history if filtered_history is not None else self.current_user.history

        if history_data:
            for item in history_data:
                try:
                    if "|" in item and len(item.split("|")) == 4:
                        dt, t_type, amt, bal = item.split("|")
                        line = f"{dt:<22}{t_type:<28}{amt:<18}{bal:<20}\n"
                        history_box.insert("end", line)
                    else:
                        history_box.insert("end", item + "\n")
                except Exception:
                    history_box.insert("end", item + "\n")
        else:
            history_box.insert("end", "\nNo transactions found.\n")

        history_box.insert("end", "=" * 90 + "\n")
        history_box.configure(state="disabled")

    def search_history(self):
        search_date = self.search_entry.get().strip()

        if not search_date:
            messagebox.showerror("Error", "Enter a date to search")
            return

        filtered = [item for item in self.current_user.history if search_date in item]

        if filtered:
            self.show_history(filtered)
        else:
            messagebox.showinfo("No Result", "No transaction found on this date")

    def download_pdf(self):
        filename = generate_passbook_pdf(self.current_user)
        messagebox.showinfo("PDF Saved", f"Passbook saved as:\n{filename}")

    def logout(self):
        self.current_user = None
        self.create_login_screen()


if __name__ == "__main__":
    root = ctk.CTk()
    app = BankingApp(root)
    root.mainloop()