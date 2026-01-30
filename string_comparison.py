# because strings are immutable!

s = "cat"
# s[0] = "r"
s = "r" + s[1:]
print(s)

s1 = "bob"
s2 = "banana"
print(s1 < s2)

s1 = "BOB"
s2 = "bob"
print(s1 > s2)

# in operator checks is a string is part of another
print("ana" in "banana") # true
print("Ana" in "banana") # false

