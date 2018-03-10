#! /usr/local/bin/python3
# _*_ encoding=utf-8 _*_

import random

def main():
    print('start')
    grid_size = (31, 41)
    try:
        f = open('rgb.txt','w')
    except IOError:
        print('can\'t create rgb.txt')
        return
    r_grid = []
    b_grid = []
    g_grid = []
    row = 0
    while row<grid_size[0]:
        temp_r_row = []
        temp_g_row = []
        temp_b_row = []
        col = 0
        while col<grid_size[1]:
            temp_r_row.append(random.randint(0,255))
            temp_g_row.append(random.randint(0,255))
            temp_b_row.append(random.randint(0,255))
            col+=1
        r_grid.append(temp_r_row)
        b_grid.append(temp_b_row)
        g_grid.append(temp_g_row)
        row+=1
    
    f.write('R grid info:\n')
    for row_array in r_grid:
        for col_num in row_array:
            f.write('%3d '%col_num)
        f.write('\n')
    f.write('G grid info:\n')
    for row_array in g_grid:
        for col_num in row_array:
            f.write('%3d '%col_num)
        f.write('\n')  
    f.write('B grid info:\n')    
    for row_array in b_grid:
        for col_num in row_array:
            f.write('%3d '%col_num)
        f.write('\n') 
    
    f.close()
    print('end')
    



if __name__ == '__main__':
    main()