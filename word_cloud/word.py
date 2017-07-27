# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import codecs
from wordcloud import WordCloud

#根据已经分好词的文本写出词云
__author__ = 'YangXiangjie'

text = codecs.open(r'love.txt', 'r', encoding='utf-8').read()
#匹配的图片形状
mask = np.array(Image.open('image/love.jpg'))
wc = WordCloud()
wc = WordCloud(background_color='white', max_words=2000, mask=mask, font_path='font/叶立群几何体.ttf',
               width=800, height=400)
wc.generate(text)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('save.png')