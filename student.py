from datetime import datetime

class Transaction:
    def __init__(self, amount, narration,transaction_type):
        self.timestamp = datetime.now()
        self.amount = amount
        self.narration = narration
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m -%d -%H -%M -%S')}| {self.transaction_type.capitalize()}| {self.narration}| Amount:{self.amount}"
    

class Account():
       
    def __init__(self,owner,min_balance):
            self.owner = owner
            self.min_balance = min_balance
            self.loan = 0
            self.frozen = False
            self.closed = False
            self.transactions = []

    def get_loan_balance(self):
            return self.loan
        
    def is_frozen(self):
            return self.frozen
        
    def is_closed(self):
            return self.closed
        
    def get_balance(self):
        total = 0
        for t in self.transactions:
            if t.transaction_type in ["deposit", "loan_granted", "intrest", "transfer_in"]:
                total+=t.amount
            elif t.transaction_type in ["withdraw", "loan_repaid", "transfer_out"]:
                total -=t.amount
        return total
        
    def check_status(self):
            if self.closed:
                return "Account is closed"
            if self.frozen:
                return "Account is frozen"
            return None
        
    def deposit(self,amount):
            if self.check_status():
                return self.check_status()
            if amount <= 0:
                return "Deposit amount must be positive"
            self.transactions.append(Transaction(amount,"Deposit made", "deposit"))
            return f"Deposited {amount}, new balance is {self.get_balance()}"
           

        
    def withdraw(self,amount):
            if self.check_status():
                return self.check_status()
            if amount <= 0:
                return "Withdraw amount must be positive"
            if self.get_balance()-amount <self.min_balance:
                return f"Cannot withdraw:Minimum balance of {self.min_balance} required"
            self.transactions.append(Transaction(amount,"Withdraw made", "withdrawal"))
            return f"Withdraw {amount}, new balance is {self.get_balance()}"
        

    def transfer_funds(self, amount, target_account):
            if self.check_status():
                return self.check_status()
            if target_account.is_closed():
                return "Target account is closed."
            if target_account.is_frozen():
                return "Target account is frozen."
            if amount <= 0:
                return "Transfer amount must be positive."
            if self.get_balance() - amount < self.min_balance:
                return f"Minimum balance of {self.min_balance} required."
            self.transactions.append(Transaction(amount, f"Transfer to {target_account.owner}", "transfer_out"))
            target_account._Account.transactions.append(Transaction(amount, f"Transfer from {self.owner}", "transfer_in"))
            return f"Transferred {amount} to {target_account.owner}. New balance: {self.get_balance()}."
        

    def request_loan(self, amount):
            if self.check_status():
                return self.check_status()
            if amount <= 0:
                return "Loan amount must be positive."
            self.loan += amount
            self.transactions.append(Transaction(amount, "Loan granted", "loan_granted"))
            return f"Loan of {amount} granted. Balance: {self.get_balance()}, Loan balance: {self.loan}."
        
    def repay_loan(self, amount):
            if self.check_status():
                return self.check_status()
            if self.loan ==0:
                return "No loan to repay"
            if amount <=0:
                return "The amount must be positive"
            if amount> self.get_balance():
                return "Insufficient funds"
            repay_amount = min(amount,self.loan)
            self.loan -=repay_amount
            self.transactions.append(Transaction(repay_amount, "Loan repayed", "loan_repaid"))
            return f"Repaid {repay_amount}. Loan balance:{self.loan}, New balance: {self.get_balance()}"
        
    def interest_calculation(self):
            if self.check_status():
                return self.check_status()
            interest = self.get_balance()*0.05
            self.transactions.append(Transaction(round(interest,2), "Interest append", "interest"))
            return f"Interest of {round(interest,2)} applied. New balance:{self.get_balance()}"
        
    def view_account_details(self):
            return (f"Owner: {self.owner}\n" f"Balance:{self.get_balance()}\n" f"Loan Balance:{self.loan}")
        
    def change_account_owner(self,new_owner):
            if self.closed:
                return "Account closed"
            self.owner = new_owner
            return f"Accoutn owner changed to {self.owner}."
        
    def account_statement(self):
            print(f"\nStatement for {self.owner}")
            for z in self.transactions:
                print(z)
            print(f"Current balance:{self.get_balance()}")
        
    def freeze_account(self):
            if self.closed:
                return "Account is closed"
            self.frozen = False
            return "Account has been unfrozen"
        
    def set_minimum_balance(self, amount):
            if amount <0:
                return "Minimum balance cannot be negative"
            self.min_balance = amount
            return f"Minimum balance set to{self.min_balance}."
        
    def close_account(self):
            self.closed = True
            self.loan =0
            self.transactions.clear()
            self.frozen = False
            return "Account closed. All balances cleared and transactions removed"




