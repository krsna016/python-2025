# Variable, Indexing, Slicing:
print(1+1)
print(5*5)
a = 10
print(a)
b = 20
print(a+b)
print(type(a))
c = "String"
print(type(c))
k = 23.77907
print(type(k))
p = True # 1
print(type(p))
q = False # 0
print(p*q)
print(type(p*q))
print(p+q)
c = 3+8j
print(c.imag)
print(c.real)
print(c)
c = "hello"
print(c[0])
print(c[:3])
print(c[-1])
print(c[-3:-1])
print(c[-len(c):len(c)-2])
print(c[2::-1]) # -2 -> 5 and -2,-2-1=-3 ,-3-1=-4
print(c[4::-1]) # -2 -> 5 and -2,-2-1=-3 ,-3-1=-4
print(c[-2::-1])
print(c[-200::-1])
# print(c[998]) # IndexError
k = 2991
k = str(k)
print(k[1])
print(k.find("9"))
print(k.count("9"))
p = "osaasaiauauau"
print(p.count("au"))
k = p.upper()
print(k)
print(p.lower())
print(p.title())
m = "ASJAJDKdj"
print(m.capitalize())
print(m.swapcase())
l = "pwskills"
print(l[-2::-1])
