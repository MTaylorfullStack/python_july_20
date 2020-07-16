# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
class BankAccount:
    def __init__(self, int_rate, balance):
        self.account_balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.account_balance:
            print(f"You are withdrawing {amount} but only have {self.account_balance}, charging $5 fee.")
            self.account_balance -= (amount+5)
        self.account_balance -= amount
        return self
    def display_account_info(self):
        print(f"Current balance: {self.account_balance}")
        return self
    def yield_interest(self):
        amount_earned = self.account_balance * self.int_rate
        self.account_balance += amount_earned
        return self


class User:
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.account = BankAccount(int_rate, balance)
    # def make_withdrawal(self, amount):
    #     self.account.account_balance -= amount
    #     return amount
    # def display_user_balance(self):
    #     print(f"{self.name} has ${self.account.account_balance} remaining.")
    #     return self
    # def transfer_money(self, other_user, amount):
    #     other_user.account.account_balance += self.make_withdrawal(amount)
    #     print(f"{other_user.name} received ${amount} from {self.name}")
    #     return self

sean = User("Sean", .02, 1000)

liz = User("Elizabeth", .05, 500)

# sean.account_balance += 1000

# sean.transfer_money(liz, 250).display_user_balance()

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

# acct = BankAccount(.02, 100)

# acct.deposit(100).display_account_info().yield_interest().withdraw(50).display_account_info()