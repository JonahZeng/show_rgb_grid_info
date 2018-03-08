#! /usr/local/bin/python3
# _*_ encoding=utf-8 _*_

from PIL import Image
from PIL import ImageColor
import numpy as np
import matplotlib.pyplot as plt

img = Image.new('RGB',(410,310), ImageColor.getrgb('#ff0000'))
#img.show()
imgarr = np.fromstring(img.tobytes(), dtype=np.uint8)
imgarr = imgarr.reshape((img.size[1], img.size[0],3))

plt.imshow(imgarr)
plt.show()
