class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        b =f'Account owner: {self.owner}'
        a =f'Account balance: {self.balance}'
        return f'{a}\n{b}'
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Deposit Accepted\nbalance: {self.balance}')
    def withdraw(self, amount):
        if amount > self.balance:
            print('Funds Unavailable')
        else:
            self.balance = self.balance - amount
            print(f'Withdrawal Accepted\nbalance: {self.balance}')
