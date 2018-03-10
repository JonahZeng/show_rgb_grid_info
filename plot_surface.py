#! /usr/local/bin/python3
# _*_ encoding=utf-8 _*_

from PIL import Image
from PIL import ImageColor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from mpl_toolkits.mplot3d import Axes3D

def down(x, pos):
	return '%d'%(x//10)

all_random_array = []
for i in range(0,31):
	temp_row = []
	for j in range(0,41):
		temp_row.append( (np.random.randint(0,256,1,np.uint8), np.random.randint(0,256,1,np.uint8), np.random.randint(0,256,1,np.uint8)) )
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
x, y = np.meshgrid(cord_x, cord_y)
print(x.shape, y.shape)
red_z_top = np.zeros((31,41), dtype=np.uint8)
green_z_top = np.zeros((31,41), dtype=np.uint8)
blue_z_top = np.zeros((31,41), dtype=np.uint8)

for i_y in range(0,31):
    for i_x in range(0,41):
        red_z_top[i_y][i_x]=all_random_array[i_y][i_x][0]
        green_z_top[i_y][i_x]=all_random_array[i_y][i_x][1]
        blue_z_top[i_y][i_x]=all_random_array[i_y][i_x][2]
fig2 = plt.figure(2)
ax2 = fig2.gca(projection='3d')
ax2.plot_surface(x, y, red_z_top)
ax2.set_title('red')

fig3 = plt.figure(3)
ax3 = fig3.gca(projection='3d')
ax3.plot_surface(x, y, green_z_top)
ax3.set_title('green')

fig4 = plt.figure(4)
ax4 = fig4.gca(projection='3d')
ax4.plot_surface(x, y, green_z_top)
ax4.set_title('blue')
plt.show()