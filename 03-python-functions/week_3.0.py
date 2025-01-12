# def func_1(v:int)->int:
#     return v+1
# print(func_1(9)+7)

# def func_2(v:int)->int:
#     print(v+1)
# func_2(5)+8 # Will get the error

# def test_1():
#     return 1,2,3,4,"hash"
# a,b,c,d,e = test_1()
# print(d)

# def test_2(a,*args):
#     return args,a
# print(test_2([1,2,3,4],5))

# def test_2(*args,a = 10):
#     return args,a
# print(test_2([1,2,3,4],5))

# def t_1(a,b,c = 9):
#     return a,b,c
# print(t_1(1,2))

# def t_2(**kwargs):
#     return kwargs
# print(t_2(a = [1,2,3],b = {4,5,6}))

# def test_fib(n):
#     a,b = 0,1
#     for i in range(n):
#         yield a
#         a,b = b,a+b
# for i in test_fib(10):
#     print(i)

# def test_fib_1():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b
# fib = test_fib_1() # Creating Object
# for i in range(10):
#     print(next(fib))


# def counter(n):
#     count = 0
#     while count < n:
#         yield count
#         count += 1
# co = counter(10)
# for i in co:
#     print(i)
