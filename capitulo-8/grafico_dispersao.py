import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
# print(np.random.random(1) * 100)
x = np.random.random(50) * 100
y = np.random.random(50) * 100

print(x)
print(y)

# plt.scatter(x, y, c='red', marker='*')
plt.scatter(x, y, c='#D2649A', s=150, marker='d', alpha=0.3)
plt.show()

