#! /usr/local/bin/python3
# _*_ encoding=utf-8 _*_

from PIL import Image
from PIL import ImageColor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import random
from mpl_toolkits.mplot3d import Axes3D
import sys

def down(x, pos):
	return '%d'%(x//10)

def readGridStat(filename, r_in_list, g_in_list, b_in_list, r_out_list, g_out_list, b_out_list):
	try:
		f_data = open(filename, encoding='utf-8')
	except IOError:
		print('open %s fail.'%filename)
		return False
	a = f_data.readline()
	r_in_flag, r_out_flag, g_in_flag, g_out_flag, b_in_flag, b_out_flag = False, False, False, False, False, False
	
	while a!='':
		if a=='Red input grid statu data:\n':
			for i in range(31):
				temp_row_data = []
				a = f_data.readline()
				row_data = a.split()
				if len(row_data)!=41:
					print('row data number !=41')
					break
				else:
					temp_row_data = [int(x)>>4 for x in row_data]
				r_in_list.append(temp_row_data)
			if len(r_in_list)==31:
				r_in_flag = True

		if a=='Green input grid statu data:\n':
			for i in range(31):
				temp_row_data = []
				a = f_data.readline()
				row_data = a.split()
				if len(row_data)!=41:
					print('row data number !=41')
					break
				else:
					temp_row_data = [int(x)>>4 for x in row_data]
				g_in_list.append(temp_row_data)
			if len(g_in_list)==31:
				g_in_flag = True

		if a=='Blue input grid statu data:\n':
			for i in range(31):
				temp_row_data = []
				a = f_data.readline()
				row_data = a.split()
				if len(row_data)!=41:
					print('row data number !=41')
					break
				else:
					temp_row_data = [int(x)>>4 for x in row_data]
				b_in_list.append(temp_row_data)
			if len(b_in_list)==31:
				b_in_flag = True

		if a=='Red output grid statu data:\n':
			for i in range(31):
				temp_row_data = []
				a = f_data.readline()
				row_data = a.split()
				if len(row_data)!=41:
					print('row data number !=41')
					break
				else:
					temp_row_data = [int(x)>>4 for x in row_data]
				r_out_list.append(temp_row_data)
			if len(r_out_list)==31:
				r_out_flag = True

		if a=='Green output grid statu data:\n':
			for i in range(31):
				temp_row_data = []
				a = f_data.readline()
				row_data = a.split()
				if len(row_data)!=41:
					print('row data number !=41')
					break
				else:
					temp_row_data = [int(x)>>4 for x in row_data]
				g_out_list.append(temp_row_data)
			if len(g_in_list)==31:
				g_out_flag = True

		if a=='Blue output grid statu data:\n':
			for i in range(31):
				temp_row_data = []
				a = f_data.readline()
				row_data = a.split()
				if len(row_data)!=41:
					print('row data number !=41')
					break
				else:
					temp_row_data = [int(x)>>4 for x in row_data]
				b_out_list.append(temp_row_data)
			if len(b_in_list)==31:
				b_out_flag = True
		a = f_data.readline()
	#print(r_in_flag, r_out_flag, g_in_flag, g_out_flag, b_in_flag, b_out_flag)
	#检查所有数据是否都完成读取
	if r_in_flag==True and b_in_flag==True and g_in_flag==True and r_out_flag==True and g_out_flag==True and b_out_flag==True:
		return True
		

def main():
	r_in = []
	g_in = []
	b_in = []
	r_out = []
	g_out = []
	b_out = []
	if len(sys.argv)==2:
		if not readGridStat(sys.argv[1], r_in, g_in, b_in, r_out, g_out, b_out):
			print('read data error!')
			return
	


	#创建一个黑色，410*310的RGB图片
	img = Image.new('RGB',(410,310), ImageColor.getrgb('#000000'))

	for y in range(0,img.size[1]):#行
		for x in range(0,img.size[0]):#列
			img.putpixel((x,y), (r_in[y//10][x//10], g_in[y//10][x//10], b_in[y//10][x//10]))#对每一个像素赋值

	imgarr = np.fromstring(img.tobytes(), dtype=np.uint8)#转化成np.ndarray用于matplotlib显示
	imgarr = imgarr.reshape((img.size[1], img.size[0], 3))
	formatter = FuncFormatter(down)
	#fig1, ax1 = plt.subplots()
	fig1 = plt.figure(1)
	ax1 = fig1.add_subplot(111)
	ax1.imshow(imgarr)
	ax1.set_xlim(0,410)
	ax1.set_ylim(310,0)
	ax1.xaxis.set_major_formatter(formatter)
	ax1.yaxis.set_major_formatter(formatter)
	ax1.set_title('31*41 rgb grid info')
	ax1.xaxis.tick_top()
	ax1.xaxis.set_label_position('top')
	ax1.title.set_position((0.5,1.06))

	cord_x = np.arange(0, 41)
	cord_y = np.arange(0, 31)
	mesh_x, mesh_y = np.meshgrid(cord_x, cord_y)
	x, y = mesh_x.ravel(), mesh_y.ravel()

	red_z_top = np.zeros(1271, dtype=np.uint8)
	green_z_top = np.zeros(1271, dtype=np.uint8)
	blue_z_top = np.zeros(1271, dtype=np.uint8)
	it = 0
	while it<1271:
		red_z_top[it]=r_in[y[it]][x[it]]
		green_z_top[it]=g_in[y[it]][x[it]]
		blue_z_top[it]=b_in[y[it]][x[it]]
		it += 1
	z_bottom = np.zeros_like(red_z_top)


	fig2 = plt.figure(2)
	ax2 = fig2.add_subplot(111, projection='3d')
	ax2.bar3d(x, y, z_bottom, 1, 1, red_z_top, shade=True)
	ax2.set_ylim(31,0)
	ax2.set_zlim(0,255)
	ax2.set_title('red')


	fig3 = plt.figure(3)
	ax3 = fig3.add_subplot(111, projection='3d')
	ax3.bar3d(x, y, z_bottom, 1, 1, green_z_top, shade=True)
	ax3.set_ylim(31,0)
	ax3.set_zlim(0,255)
	ax3.set_title('green')

	fig4 = plt.figure(4)
	ax4 = fig4.add_subplot(111, projection='3d')
	ax4.bar3d(x, y, z_bottom, 1, 1, blue_z_top, shade=True)
	ax4.set_ylim(31,0)
	ax4.set_zlim(0,255)
	ax4.set_title('blue')

	plt.show()

if __name__=='__main__':
	main()