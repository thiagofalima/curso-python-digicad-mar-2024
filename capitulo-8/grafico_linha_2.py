

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
empresa_a = np.random.random(10) * 100
empresa_b = np.random.random(10) * 100

# plt.figure(1)
plt.plot(empresa_a, label='empresa1', c="green")
plt.legend(loc='lower center')
# plt.figure(2)
plt.plot(empresa_b, 'r--', label='empresa2')
plt.legend(loc='lower center')
plt.show()

