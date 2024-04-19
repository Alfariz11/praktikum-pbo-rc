import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self, window):
        self.window = window
        self.window.title("Login")
        self.window.geometry("200x150")

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)

        self.users = {}  

        self.username_label = tk.Label(window, text="Username")
        self.username_label.grid(row=0, column=0)
        self.username_text = tk.Entry(window)
        self.username_text.grid(row=0, column=1)

        self.password_label = tk.Label(window, text="Password")
        self.password_label.grid(row=1, column=0)
        self.password_text = tk.Entry(window, show="*")
        self.password_text.grid(row=1, column=1)

        self.login_button = tk.Button(window, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.register_button = tk.Button(window, text="Register", command=self.register)
        self.register_button.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        if self.users:
            valid_username = list(self.users.keys())[0]
            valid_password = list(self.users.values())[0]

            input_username = self.username_text.get()
            input_password = self.password_text.get()

            if input_username == valid_username and input_password == valid_password:
                messagebox.showinfo("Success", "Welcome, " + input_username)
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        else:
            messagebox.showerror("Error", "No registered users.")

    def register(self):
        register_window = tk.Toplevel(self.window)
        register_window.title("Register")
        register_window.geometry("200x150")

        self.register_username_label = tk.Label(register_window, text="Username")
        self.register_username_label.grid(row=0, column=0)
        self.register_username_text = tk.Entry(register_window)
        self.register_username_text.grid(row=0, column=1)

        self.register_password_label = tk.Label(register_window, text="Password")
        self.register_password_label.grid(row=1, column=0)
        self.register_password_text = tk.Entry(register_window, show="*")
        self.register_password_text.grid(row=1, column=1)

        self.register_confirm_password_label = tk.Label(register_window, text="Confirm Password")
        self.register_confirm_password_label.grid(row=2, column=0)
        self.register_confirm_password_text = tk.Entry(register_window, show="*")
        self.register_confirm_password_text.grid(row=2, column=1)

        self.register_button = tk.Button(register_window, text="Register", command=lambda: self.register_user(register_window))
        self.register_button.grid(row=3, column=0, columnspan=2, pady=10)

    def register_user(self, register_window):
        username = self.register_username_text.get()
        password = self.register_password_text.get()
        confirm_password = self.register_confirm_password_text.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        if username in self.users:
            messagebox.showerror("Error", "Username already exists.")
            return

        self.users[username] = password
        messagebox.showinfo("Success", "User " + username + " registered successfully.")
        register_window.destroy()

root = tk.Tk()
app = Login(root)
root.mainloop()