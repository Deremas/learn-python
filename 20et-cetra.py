# global

balance = 0

def main():
    print(f'Balance: {balance}')
    deposit(100)
    print(f'Balance: {balance}')
    withdraw(50)
    print(f'Balance: {balance}')

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount

if __name__ == "__main__":
    main()

# If  balance -= amount used in deposit and withdraw functions, it will cause an error because balance is a global variable and we are trying to modify it inside the functions without declaring it as global. To fix this, we need to declare balance as global inside the deposit and withdraw functions.
# UnboundLocalError: local variable 'balance' referenced before assignment in function 'deposit'
# UnboundLocalError: local variable 'balance' referenced before assignment in function 'withdraw'

class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        self._balance -= amount
    
def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()

# constants notation in python:
# In Python, constants are typically defined using uppercase letters with underscores separating words. This convention helps to indicate that the value is intended to be constant and should not be changed throughout the program. For example, you might define a constant for the speed of light as follows:
SPEED_OF_LIGHT = 299792458  # in meters per second
# By using uppercase letters, it is clear to other developers that SPEED_OF_LIGHT is a constant and should not be modified. However, it's important to note that Python does not enforce immutability for constants, so it's still possible to change the value of SPEED_OF_LIGHT if you choose to do so. Therefore, it's a good practice to treat constants as immutable and avoid modifying their values in your code.

class Cat:
    MEOWS = 4

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("Meow!")

cat = Cat()
cat.meow()

# type hints 29:19 min
