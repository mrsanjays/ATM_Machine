class InsufficientFundsException(Exception):
    pass
class InvalidAmountException(Exception):
    pass
class BankBalance:
    def __init__(self):
        self.__balance=10000 #private variable
    def get_balance(self):
        return self.__balance
    def set_balance(self,newamount):
        self.__balance=newamount
    def add_money(self,amount):
        x=self.get_balance()
        self.set_balance(amount+x)
        print(f"{amount} is deposited Successfully! your available Balance is {self.get_balance()}")
    def withdraw_money(self,amount):
        try:
            if amount>self.get_balance():
                raise InsufficientFundsException
            if amount<0:
                raise InvalidAmountException
            else:
                print("Collect your cash!")
                x=self.get_balance()
                self.set_balance(x-amount)
                print(f"Your Balance is {self.get_balance()}")
        except InvalidAmountException:
            print("Input can be Negative")
        except InsufficientFundsException:
            print("Insufficient Account Balance")

if __name__ == '__main__':
    exit=True
    user =BankBalance()
    while exit:
        case = int(input("""
            Press 1 to deposit
            Press 2 to withdraw
            Press 3 to Display
            Press 4 to exit
            Enter:"""))
        if case==4:
            print("Thankyou!!")
            quit()
        if case==1:
            amount=int(input("Enter amount to Deposit:"))
            user.add_money(amount)
        if case==2:
            x=user.get_balance()
            if x>0:
                amount=int(input("Enter amount to Withdraw:"))
                user.withdraw_money(amount)
            else:
                print("Your balance is Zero")
                quit()
        if case==3:
            print(f"Your Balance is {user.get_balance()}")








