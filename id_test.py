def a(s):
    print(id(s))
    s += s
    print(id(s))

s = [9]
print(s, id(s))
a(s)
print(s, id(s))


