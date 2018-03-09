#! /usr/local/bin/python3
# _*_ encoding=utf-8 _*_
from PIL import Imagefrom PIL 
import ImageColorimport numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import random
def down(x, pos):    
	'scale down x / y axis'    
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
imgarr = imgarr.reshape((img.size[1], img.size[0],3))
#plt.rcParams['xtick.bottom'] = False
#plt.rcParams['xtick.top'] = True
formatter = FuncFormatter(down)
fig, ax1 = plt.subplots()
ax1.imshow(imgarr)
ax1.set_xlim(0,410)
ax1.set_ylim(310,0)
ax1.xaxis.set_major_formatter(formatter)
ax1.yaxis.set_major_formatter(formatter)
ax1.set_title('31*41 rgb grid show')
ax1.xaxis.tick_top()ax1.xaxis.set_label_position('top')
print(ax1.title.get_position())ax1.title.set_position((0.5,1.06))
plt.show()
