import copy

a = [1, 2, 3, 4, 5]
print(id(a))

b = a

print(id(b))

b.pop()

print(a)
print(b)

c = copy.deepcopy(a)

print(id(a))
print(id(c))

c.extend([5, 6])

print(a)
print(c)
