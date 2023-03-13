#Q9
import numpy as np
import matplotlib.pyplot as plt



y1 = x * np.sin(x)
y2 = x**2 * np.sin(x)
y3 = x**3 * np.sin(x)
y4 = x**4 * np.sin(x)

plt.subplot(2,2,1)
plt.plot(x, y1, label='xsin(x)')
plt.subplot(2,2,2)
plt.plot(x, y2, label='x^2sin(x)')
plt.subplot(2,2,3)
plt.plot(x, y3, label='x^3sin(x)')
plt.subplot(2,2,4)
plt.plot(x, y4, label='x^4sin(x)')


plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()