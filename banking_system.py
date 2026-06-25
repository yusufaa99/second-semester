# this project is implemented with respect to encapsulation understanding

class Account:

    def __init__(self):
        self.balance = 2000
        self.__loan_balance = 50000
    def __update_balance(selfl, amount):
        selfl.balance += amount 

    def _show_balance(self):
        print(f"Balance: {self.balance}")
    
    def deposite(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            self._show_balance()
        else:
            print(f"Invalid amount: {self.amount}")

    def get_loan_balance(self):
        return f"Loan Balnce: {self.__loan_balance}"
    
    def set__loan_balance(self, amount):
        if amount > 0:
            self.__loan_balance += amount
        else:
            print(f"Invalid Loan Amount: {amount}")

acc = Account()

acc._show_balance()
acc.deposite(3000)

print(acc.get_loan_balance())
acc.set__loan_balance(-25000)
print(acc.get_loan_balance())

