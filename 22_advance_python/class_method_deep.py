class Database:
    users = {} # storage

    def __init__(self,id,name):  # storing method
            self.users[id] = name

    @classmethod 
    def add_unique_user(self,id,name): # class method to check uniquesess and calling 'storing method'
        if id not in self.users:
            return self(id , name)
        else:
             pass
        
        
u1 = Database.add_unique_user(1,"harry") # this calls the 'class method'
u2 = Database.add_unique_user(2,"john")
u3 = Database.add_unique_user(3,"harry")
u4 = Database.add_unique_user(4,"jack")
u5 = Database.add_unique_user(4,"henry") # this test should not pass since id 4 already stored previously



print(Database.users)





