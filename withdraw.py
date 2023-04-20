import tkinter as tk

class BlackjackGUI:
    def __init__(self, balance):
        self.balance = balance
        self.window = tk.Tk()
        self.window.title("Blackjack Game")
        self.window.geometry("300x200")
        
        self.balance_label = tk.Label(self.window, text="Balance: ${}".format(self.balance))
        self.balance_label.pack(pady=10)
        
        self.withdraw_button = tk.Button(self.window, text="Withdraw", command=self.withdraw_balance)
        self.withdraw_button.pack(pady=10)
        
        self.window.mainloop()
        
    def withdraw_balance(self):
        self.balance = 0
        self.balance_label.config(text="Balance: ${}".format(self.balance))
        self.thank_you_label = tk.Label(self.window, text="Thanks for playing!")
        self.thank_you_label.pack(pady=10)
        
game = BlackjackGUI(100)
