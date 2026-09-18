import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.subplot(2,1,1)

plt.plot(xpoints,ypoints,linestyle='dotted')

#plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2,1,2)
plt.barh(x,y)
plt.show()