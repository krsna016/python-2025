# Mutability and Imutability:
s = "Anurag"
t = "Pareek"
l = [1,2,3.99,'p',4,'okay',True] # Collection <- List data type
print(type(s))
print(type(l))
print(s[3])
print(l[4])
print(l[-3])
l[1] = 100
print(l)
l[0] = "Anurag" # List is mutable
print(l)
# s[2] = "a" # Becouse 'String' is immutable