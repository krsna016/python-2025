# def test():
#     print("This is the start of my function.")
#     print("This is my function to test.")
#     print("This is the end of my function.")
# test()



# def deco(func):
#     def inner_deco():
#         print("This is the start of my function.")
#         func()
#         print("This is the end of my function.")
#     return inner_deco()
# # def test_1():
# #     print(6+9)
# # deco(test_1)
# @deco
# def test_1():
#     print(6+9)



import time
def deco_timer(func):
    def inner_func():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return inner_func
@deco_timer
def test_2():
    print(55+78)
test_2()
@deco_timer
def test_3():
    for i in range(100000000):
        pass
test_3()