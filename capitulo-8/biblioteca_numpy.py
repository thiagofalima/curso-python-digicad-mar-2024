import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7])

print(a)

print(type(a))

print(a.dtype)
print(a.shape)
print(a.size)

print(a[2])
print(a[2:])
print(a[1:4])

a[2] = 10

print(a)
print(a.dtype)

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(m)
print(type(m))

print(m.shape)
print(m.ndim)
print(m.size)
print(m.dtype)

matriz_zeros = np.zeros((2, 3))

print(matriz_zeros)
print(type(matriz_zeros))
print(matriz_zeros.shape)

matriz_uns = np.ones((2, 3))

print(matriz_uns)
print(type(matriz_uns))
print(matriz_uns.shape)

b = np.array(range(10))
print(b)

c = np.linspace(20, 100, 10)

print(c)
print(c.size)