import numpy as np
import matplotlib.pyplot as plt

file = np.loadtxt('Gaussian.dat', skiprows=1)
x = file[:, 0]
y = file[:, 1]
for element in x, y:
    element = element * 0
    print(element)
print(x)
print(y)
plt.plot(x, y)
plt.show()
