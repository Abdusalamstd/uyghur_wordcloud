# Uyghur Text Wordcloud Generator  维文词云生成程序
# ئۇيغۇرچە سۆزلۈكلەرگە سۆز بۇلۇتى ياساش  ئۇسۇلى
## Feature: Uyghur text written from **Right to Left**
### how to use ?قانداق ئىشلىتىلىدۇ؟
Environment ： Python3.7\
There are only have two files, **soz.py** and **abc.txt**. You can download this files and run **soz.py** on your PC you can get word cloud.You can also change **abc.txt** file and put your word in this file, You will get personal word cloud.\
ھۆججەتلەر: soz.py , abc.txt\ 
كود ھۆججىتى: soz.py \ \
ئىجرا مۇھېتى: Python3.7 \ \
يۇقارقى ئىككى ھۆججەتنى چۈشۈرۈپ،ئىجرا قىلسىڭىزلا سۆز بۇلۇتقا ئېرىشەلەيسىز. تېكسىت ھۆججىتى ئىچىگە سىز ئۆزىڭىزنىڭ سۆزلۈكلىرىنى كىرگۈزسىڭىز بولىدۇ. \ \


### Code anatomy
```python
# -*- coding: utf8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt 
from bidi.algorithm import get_display
import arabic_reshaper
path_txt='a.txt'
f = open(path_txt,'r',encoding='UTF-8').read()
reshaped_text = arabic_reshaper.reshape(f)
f = get_display(reshaped_text)
wc= WordCloud(font_path="ALKATIP Elipbe.ttf",background_color="white",width=1000,height=880)
wc.generate(f)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
```
### كود چۈشەندۈرۈش
```python
# -*- coding: utf8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt 
from bidi.algorithm import get_display
import arabic_reshaper
path_txt='a.txt'
f = open(path_txt,'r',encoding='UTF-8').read()
reshaped_text = arabic_reshaper.reshape(f)
f = get_display(reshaped_text)
wc= WordCloud(font_path="ALKATIP Elipbe.ttf",background_color="white",width=1000,height=880)
wc.generate(f)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
```













