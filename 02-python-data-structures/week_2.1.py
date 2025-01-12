# List,Tuple:
l = [1,2.3982,False,"Hello",[1,2,3],3+9j]
print(type(l))
print(l[5])
print(l[3:9])
print(l[-4::-1])
print(l[-1])
print(l[::2])
s = "PwSkills"
s = (list(s))
print(l+s)
print(l[3][1:3])
print(str(l[1])+l[3])
print(len(l))
l.append(7)
print(l)
print(l[4][1])
l.extend("ooo")
print(l)
# l.extend(5) # Error
l.extend([5]) # Error
print(l)

p = [1,2,3]
p.insert(0,2)
print(p)
p.insert(-1,9)
print(p)
p.pop()
print(p)
p.pop(1)
k = p.pop(1)
print(k)
print(p)
del p[0]
print(p)
m = list("abccdef")
m.remove("c")
print(m)
m.extend([[1,2,3]])
print(m)
del m[6][1]
print(m)
m[-1].remove(1)
print(m)
m.reverse()
print(m)
p = ["a","A"] # Compare using ASCII
p.sort()
print(p)
o = set()
print(type(o))
o = {}
print(type(o))
s = "7877"
print(type(s))
s = {(1,2,3),(1,2,3)}
# print(s[0])
d = {'name':'anurag',"num":438732382,32:[232,32],("sd","123"):(1,1,1,2,3),True:123}
print(d[True])
print(d[("sd","123")])
print(d['name'])
print(d[32])
d["abc"] = "a1"
del d["name"]
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))
print(d.pop("abc"))
print(d)
print(str(d))