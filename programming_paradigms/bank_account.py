class BankAccount :
    def __init__(self, account_balance ) :
        self.account_balance = account_balance 
        # account_balance = 0
    def deposit(self, amount):
        # amount = int(input("Enter the amount to deposit: "))
        self.account_balance += amount
    def withraw(self, amount, account_balance):
        amount = int(input("Enter the amount to withdraw: "))
        if account_balance >= amount:
            
            account_balance -= amount
            return True
        else :
            return False
        
    def display_balance (self):
        print(f"The balance of your account is :{self.account_balance}.")
    

        
    