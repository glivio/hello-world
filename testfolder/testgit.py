import matplotlib.pyplot as plt
import numpy as np

y = np.random.randint(0,10,100)
x = np.linspace(0,10,100)
y = 0.5*x**2

plt.scatter(x,y)
plt.show()

# added some test