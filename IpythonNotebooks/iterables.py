# a string is an iterable
myname = "janet"
x = 1 

for i in myname:
    print(f"letter {x} = {i}")
    x += +1

print(f"the character in the 4th position of {myname} is {myname[3]}")

y = 8
# https://pynative.com/python-range-function/
for i in range(y, 2, -2):
    print(i)

mytuple_0 = ("A" ,"B")
mytuple_1 = ("C" ,"D")
mytuple_0 = mytuple_0 + mytuple_1
print(mytuple_0)

for character in mytuple_0:
    print(character)