# Conditions:
a = int(input())
if a>10:
    print("a is greater than 10")
else:
    print("Well")

k = "hello"
if k == "Ok":
    print("Ok")
elif k == "hello":
    print("Hello")
else:
    print('Well')
inp = input()
print(inp)
print(int(inp))

# Loops:
i = 8
j = 1
while j<i:
    print("Running")
    j += 1
    if j == 2:
        break
else:
    print("Hello")

for i in range(1,9):
    print("Running")

name = "anurag"
for i in name:
    print(i)

list_1 = [1,2,3.09,4.0,"a",True,3j]
for i in list_1:
    print(type(i))

for i in range(1,11):
    if i == 4:
        break
    else:
        print(i)

for i in range(1,11):
    if i == 4:
        continue
    else:
        print(i)

i = 1
while i < 10:
    print(i)
    if i ==4:
        break
    i+=1
else:
    print("Ok")

p = 1
while p <7:
    print(p)
    p += 1
    if p == 3:
        continue
else:
    print("hello")