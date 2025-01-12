# Conditional Statements:
# marks = int(input())
# if marks > 0:
#     print("Hello")
l = list(range(11))
l1 = []
for i in l:
    l1.append(i+1)
print(l1)
l2 = ["Hello","World","world1","pwskills"]
l3 = []
for i in l2:
    l3.append(i.upper())
print(l3)
k = [1,2,3,"a","b",12.9]
f=[]
n=[]
s=[]
for i in k:
    if type(i) == int:
        n.append(i)
    elif type(i) == float:
        f.append(i)
    else:
        s.append(i)
print(f,n,s)