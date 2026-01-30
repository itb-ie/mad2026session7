
text = "Hello World"
print(text)
text = 'Hello World 2' # single vs double
print(text[4])
print(len(text)) # length of the text
text = ""
print(len(text))

text = "Bob"
print(text[-1]) # last character in the string
print(text[-3])

# print(text[3]) # this is an error
print(text[6//3])

# you can add 2 strings
s1 = "hello"
s2 = "bye"
print(s1 + s2)
print(s1*4)

# string is iterable, you can use for over it
s1 = "Hello my name is Bob"
for c in s1:
    print(c)

s1 = "I like to give hi fives"
# print this string, but replace 'i' with 'y'
# Y lyke to gyve hy fyves
s1_new = ""
for c in s1:
    if c == "i":
        s1_new += "y"
    elif c == "I":
        s1_new += "Y"
    else:
        s1_new = s1_new + c # same as +=
print(s1_new)

s1 = "I like to give hi fives"
for c in s1:
    if c == "i":
        print("y", end="")
    elif c == "I":
        print("Y", end="")
    else:
        print(c, end="")
print()

