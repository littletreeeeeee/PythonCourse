import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
x3 = np.linspace(0.1, 10.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)

plt.subplot(3, 1, 1)
plt.plot(x1, y1, 'yo-')
plt.title('')
plt.ylabel('figure')

plt.show()