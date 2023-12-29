class User:
    def __init__(self):
        # Private attributes with double underscores
        self.__name = input("Name: ")
        self.__age = int(input("Age: "))
        self.__gender = input("Gender: ")
        self.__initial_amount = int(input("Enter the amount you want to open bank account with: "))

    def get_user_info(self):
        # Public method to access and display user information
        print(f'User name: {self.__name}')
        print(f'Age: {self.__age}')
        print(f'Gender: {self.__gender}')

    def get_user_name(self):
        # Public method to access user's name
        return self.__name

    def get_initial_balance(self):
        # Public method to access the initial balance
        return self.__initial_amount


class Bank(User):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (User)
        self.balance = self.get_initial_balance()  # Initialize balance with the initial amount

    def view_balance(self):
        # Public method to view the account balance
        print(f'Hi {self.get_user_name()},'
              f'Your account balance is: {self.balance}')

    def deposit(self):
        # Public method to deposit money into the account
        deposit_amount = int(input("Enter the amount you want to deposit: "))
        self.balance += deposit_amount
        print(f'Amount {deposit_amount} successfully deposited')
        print(f'Your account balance is {self.balance}')

    def withdraw(self):
        # Public method to withdraw money from the account
        withdraw_amount = int(input("Enter the amount you want to withdraw: "))

        if self.balance >= withdraw_amount:
            print(f"Amount {withdraw_amount} successfully withdrawn")
            self.balance = self.balance - withdraw_amount
            print(f'Your account balance is {self.balance}')
        else:
            print("Your balance is insufficient to withdraw")

    def transfer(self, target_account):
        # Public method to transfer money to another account
        target_amount = int(input("Enter the amount to be transferred: "))

        if self.balance >= target_amount:
            target_account.balance += target_amount
            print(f'Amount {target_amount} successfully transferred ')
            self.balance -= target_amount
            print(f'Your account balance is {self.balance}')
        else:
            print("Your balance is insufficient to transfer")



