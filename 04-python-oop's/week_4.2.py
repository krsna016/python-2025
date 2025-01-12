# class test:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

# t = test(20,40)
# t.a = 100 # User is able to change the inner variables
# print(t.a)
# print(t.b)



# class car:
#     def __init__(self,year,make,model,speed):
#         self.__year = year
#         self.__make = make
#         self.__model = model
#         self.__speed = 0
#     def set_speed(self,speed):
#         self.__speed = 0 if speed <= 0 else speed
#     def get_speed(self):
#         return self.__speed
# c = car(2012,999,"Ab20",80)
# c.set_speed(10)
# print(c.get_speed())
# c.set_speed(-1110)
# print(c.get_speed())



class bank_account:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance = self.__balance + amount
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient amount")
    def get_balance(self):
        return self.__balance
user = bank_account(1000)
print(user.get_balance())
user.deposit(1050)
print(user.get_balance())
user.withdraw(2000)
print(user.get_balance())



