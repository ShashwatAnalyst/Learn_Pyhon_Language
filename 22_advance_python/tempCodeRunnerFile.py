class Account:
    def __init__(self ,  userid, password, balance):
        self.userid = userid
        self.__password = password
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    def deduct_balance(self , password , deduct):
        if self.__password == password:
            new_balance = self.__balance - deduct
            self.__balance = new_balance
            print(f"Amount of {deduct} has been deducted from your account id {self.userid}, current balance is {self.__balance}")
        else:
            print(f"Incorrect Password")

    

harry = Account("harry123","password",5000)
print(harry.balance)
password = str(input("Enter password: "))
deduct = int(input("Enter Amount: "))
harry.deduct_balance(password,deduct)
