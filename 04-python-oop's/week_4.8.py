# print(dir(len))

# a = 10
# a = a + 5
# print(a)

# a = 10
# a = a.__add__(5)
# print(a)

# class pwskills:
#     def __new__(cls):
#         print("This is my new")
#     def __init__(self):
#         print("This is my 'init'")
#         self.mobile_num = 2183328339
# pw = pwskills()
# pw.mobile_num

class pwskills:
    def __init__(self):
        self.mobile_num = 2183328339
    def __str__(self) -> str:
        return "This is My Magic call of str"
pw = pwskills()
print(pw) # When initially we call this we get an object code but later after
          # calling dunder func named __str__ we get a meaningfull message.