class User:
    def __init__(self):
        self.name = input("Name: ")
        self.age = int(input("Age: "))
        self.gender = input("Gender: ")
        self.initial_amount = int(input("Enter the amount you want to open bank account with: "))

    def get_user_info(self):
        print(f'User name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')


class Bank(User):
    def __init__(self):
        super().__init__()
        self.balance = self.initial_amount

    def view_balance(self):
        print(f'Hi {self.name},'
              f'Your account balance is: {self.balance}')

    def deposit(self):
        deposit_amount = int(input("Enter the amount you want to deposit: "))
        self.balance += deposit_amount
        print(f'Amount {deposit_amount} successfully deposited')
        print(f'Your account balance is {self.balance}')

    def withdraw(self):
        withdraw_amount = int(input("Enter the amount you want to withdraw: "))

        if self.balance >= withdraw_amount:
            print(f"Amount {withdraw_amount} successfully withdrawn")
            self.balance = self.balance - withdraw_amount
            print(f'Your account balance is {self.balance}')
        else:
            print("Your balance is insufficient to withdraw")

    def transfer(self, target_account):
        target_amount = int(input("Enter the amount to be transferred: "))

        if self.balance >= target_amount:
            target_account.balance += target_amount
            print(f'Amount {target_amount} successfully transferred ')
            self.balance -= target_amount
            print(f'Your account balance is {self.balance}')
        else:
            print("Your balance is insufficient to transfer")



