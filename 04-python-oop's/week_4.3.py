# class parent_test:
#     def test_1(self):
#         return "This is my first class"
# class child_test(parent_test):
#     pass
# print(child_test().test_1())



# class class_1:
#     def test_class_1(self):
#         return "This is a method from class 1"
# class class_2(class_1):
#     def test_class_2(self):
#         return "This is a method from class 2"
# class class_3(class_2):
#     def test_class_3(self):
#         return "This is a method from class 3"
# c_3 = class_3()
# print(c_3.test_class_1())
# print(c_3.test_class_2())
# print(c_3.test_class_3())



class class_1:
    def test_class_1(self):
        return "This is class 1"
class class_2:
    def test_class_2(self):
        return "This is class 2"
class class_3(class_1,class_2):
    pass
c = class_3()
print(c.test_class_1())
print(c.test_class_2())


