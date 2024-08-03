class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrawal successful. New balance: ${self.balance:.2f}"

    def transfer(self, amount, target_account):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        target_account.balance += amount
        return f"Transfer successful. Your new balance: ${self.balance:.2f}"

    def check_balance(self):
        return f"Your current balance is: ${self.balance:.2f}"

def ussd_menu():
    print("Welcome to USSD Banking")
    print("1. Deposit")
    print("2. Transfer")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

def main():
    account = BankAccount(account_number="123456789")
    target_account = BankAccount(account_number="987654321")

    while True:
        ussd_menu()
        choice = input("Please select an option: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            print(account.deposit(amount))

        elif choice == '2':
            amount = float(input("Enter amount to transfer: "))
            print(account.transfer(amount, target_account))

        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(amount))

        elif choice == '4':
            print(account.check_balance())

        elif choice == '5':
            print("Thank you for using USSD Banking.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
