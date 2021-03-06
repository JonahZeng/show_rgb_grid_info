#! /usr/local/bin/python3
# _*_ encoding=utf-8 _*_

from PIL import Image
from PIL import ImageColor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import random
from mpl_toolkits.mplot3d import Axes3D

def down(x, pos):
	return '%d'%(x//10)

all_random_array = []
for i in range(0,31):
	temp_row = []
	for j in range(0,41):
		temp_row.append( (random.randint(0,255), random.randint(0,255), random.randint(0,255)) )
	all_random_array.append(temp_row)

img = Image.new('RGB',(410,310), ImageColor.getrgb('#000000'))
#img.show()
for y in range(0,img.size[1]):
	for x in range(0,img.size[0]):
		img.putpixel((x,y), all_random_array[y//10][x//10])

imgarr = np.fromstring(img.tobytes(), dtype=np.uint8)
imgarr = imgarr.reshape((img.size[1], img.size[0], 3))
formatter = FuncFormatter(down)
fig1, ax1 = plt.subplots()
ax1.imshow(imgarr)
ax1.set_xlim(0,410)
ax1.set_ylim(310,0)
ax1.xaxis.set_major_formatter(formatter)
ax1.yaxis.set_major_formatter(formatter)
ax1.set_title('31*41 rgb grid info')
ax1.xaxis.tick_top()
ax1.xaxis.set_label_position('top')
ax1.title.set_position((0.5,1.06))

cord_x = np.arange(0,41)
cord_y = np.arange(0,31)
mesh_x, mesh_y = np.meshgrid(cord_x, cord_y)
x, y = mesh_x.ravel(), mesh_y.ravel()

red_z_top = np.zeros(1271, dtype=np.uint8)
green_z_top = np.zeros(1271, dtype=np.uint8)
blue_z_top = np.zeros(1271, dtype=np.uint8)
it = 0
while it<1271:
	red_z_top[it]=all_random_array[y[it]][x[it]][0]
	green_z_top[it]=all_random_array[y[it]][x[it]][1]
	blue_z_top[it]=all_random_array[y[it]][x[it]][2]
	it += 1
z_bottom = np.zeros_like(red_z_top)

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111, projection='3d')
ax2.bar3d(x, y, z_bottom, 1, 1, red_z_top, shade=True)
ax2.set_title('red')

fig3 = plt.figure(3)
ax3 = fig3.add_subplot(111, projection='3d')
ax3.bar3d(x, y, z_bottom, 1, 1, green_z_top, shade=True)
ax3.set_title('green')

fig4 = plt.figure(4)
ax4 = fig4.add_subplot(111, projection='3d')
ax4.bar3d(x, y, z_bottom, 1, 1, green_z_top, shade=True)
ax4.set_title('blue')

plt.show()
