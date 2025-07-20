class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def transfer(self, amount, target_account):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                target_account.balance += amount
                print(f"Transferred ${amount:.2f} to account {target_account.account_number}. "
                      f"Your new balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Transfer amount must be positive.")

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Owner: {self.owner_name}")
        print(f"Balance: ${self.balance:.2f}")

# Example usage
if __name__ == "__main__":
    # Create two bank accounts
    account1 = BankAccount("1001", "Alice", 1000)
    account2 = BankAccount("1002", "Bob", 500)

    # Test deposit
    account1.deposit(200)  # Deposited $200.00. New balance: $1200.00
    account1.deposit(-50)  # Deposit amount must be positive.

    # Test withdrawal
    account2.withdraw(100)  # Withdrew $100.00. New balance: $400.00
    account2.withdraw(500)  # Insufficient funds.
    account2.withdraw(-20)  # Withdrawal amount must be positive.

    # Test transfer
    account1.transfer(300, account2)  # Transferred $300.00 to account 1002. Your new balance: $900.00
    account1.transfer(1000, account2)  # Insufficient funds for transfer.
    account1.transfer(-50, account2)  # Transfer amount must be positive.

    # Display account details
    account1.display_info()
    account2.display_info()