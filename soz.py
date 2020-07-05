# -*- coding: utf8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt 
from bidi.algorithm import get_display
import arabic_reshaper
path_txt='abc.txt'
f = open(path_txt,'r',encoding='UTF-8').read()
reshaped_text = arabic_reshaper.reshape(f)
f = get_display(reshaped_text)
wc= WordCloud(font_path="ALKATIP Elipbe.ttf",background_color="white",width=1000,height=880)
wc.generate(f)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
