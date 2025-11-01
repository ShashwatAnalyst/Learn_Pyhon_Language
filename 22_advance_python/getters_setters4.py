# this is not considerd a good code 
# this code is just for understanding purpose of getters and setters

class Account:
    def __init__(self ,  userid, password, balance):
        self.userid = userid
        self.__password = password
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self , deduct):
        password = str(input("Enter Password: "))
        if self.__password == password:
            new_balance = self.__balance - deduct
            self.__balance = new_balance
            print(f"Amount of {deduct} has been deducted from your account id {self.userid}, current balance is {self.__balance}")
        else:
            print(f"Incorrect Password")

    

harry = Account("harry123","password",5000)
print(harry.balance)
harry.balance = int(input("Enter Amount: "))