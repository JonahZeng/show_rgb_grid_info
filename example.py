import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# setup the figure and axes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# fake data
_x = np.arange(4)
print(type(_x))
print(_x)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
print(type(_xx))
print(_xx)
print(_yy)
x, y = _xx.ravel(), _yy.ravel()
print(type(x))
print('x:',x)
print('y:',y)

top = x + y
print('top:',top)
bottom = np.zeros_like(top)
print('bottom:',bottom)
width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title('Shaded')

ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
ax2.set_title('Not Shaded')

plt.show()