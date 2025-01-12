# l = [1,2,4,6,7,9]
# def sqr(l):
#     k = []
#     for i in l:
#         k.append(i**2)
#     return k
# print(sqr(l))


# p = map(lambda k:k**2,l)
# print(list(p))


# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# k = list(map(lambda x,y:x+y,l1,l2))
# print(k)

# s = "PwskillS"
# k = list(map(lambda x:x.upper(),s))
# print

from functools import reduce
# l = [1,2,3,4,6]
# k = reduce(lambda x,y: x*y,l)
# print(k)

# l1 = [1,2,3,4,5]
# k = reduce(lambda x,y : x if x>y else y,l1)
# print(k)        


# def div_3(x):
#     if x%3 == 0:
#         return True
# # k = filter(div_3,[1,2,3,5,7,8,9,12])
# k = filter(lambda x:x%3==0,[1,2,3,5,7,8,9,12])
# print(list(k))

# p = [-1,2,-77,6,6,7,3]
# print(list(filter(lambda x: x<0,p)))

q = ["anurag","Krsna","Radha"]
print(list(filter(lambda x:len(x)<6,q)))