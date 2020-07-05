# Uyghur Text Wordcloud Generator  维文词云生成程序
# ئۇيغۇرچە سۆزلۈكلەرگە سۆز بۇلۇتى ياساش  ئۇسۇلى
## Feature: Uyghur text written from **Right to Left**
### how to use ?قانداق ئىشلىتىلىدۇ؟
Environment ： Python3.7\
There are only have two files, **soz.py** and **abc.txt**,and one font file for Uyghur language **ALKATIP Elipbe.ttf** (Font file is necessary). You can download this files and run **soz.py** on your PC you can get word cloud.You can also change **abc.txt** file and put your word in this file, You will get personal word cloud.\
ھۆججەتلەر: soz.py , ALKATIP Elipbe.ttf,abc.txt\ 
كود ھۆججىتى: soz.py \ \
ئىجرا مۇھېتى: Python3.7 \ \
يۇقارقى ئۈچ ھۆججەتنى چۈشۈرۈپ،ئىجرا قىلسىڭىزلا سۆز بۇلۇتقا ئېرىشەلەيسىز. تېكسىت ھۆججىتى ئىچىگە سىز ئۆزىڭىزنىڭ سۆزلۈكلىرىنى كىرگۈزسىڭىز بولىدۇ ، بۇيەردە مەن  بىر ئەلكاتىپ خەت نۇسخا ھۆججىتىنىمۇ يوللاپ قويدۇم،چوقۇم بولۇشى شەرت. \ \


### Code anatomy
```python
# -*- coding: utf8 -*-
from wordcloud import WordCloud
#import word cloud module
import matplotlib.pyplot as plt 
#import matplot module soas to plot word_cloud picture
from bidi.algorithm import get_display
# bidi algirithm ,This is importang module for Right To Left (RTL)written language
import arabic_reshaper
# rehspae RTL text
path_txt='a.txt'
#text file path
f = open(path_txt,'r',encoding='UTF-8').read()
# open text file in UTF-8 mood
reshaped_text = arabic_reshaper.reshape(f)
f = get_display(reshaped_text)
# bidi & reshape RTL text
wc= WordCloud(font_path="ALKATIP Elipbe.ttf",background_color="white",width=1000,height=880)
# picture window size and Font settings
wc.generate(f)
# generate word cloud
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
# plot image
```
### كود چۈشەندۈرۈش
```python
# -*- coding: utf8 -*-
from wordcloud import WordCloud
#سۆز بۇلۇت بولىقى
import matplotlib.pyplot as plt 
#مەت پلوت رەسىم بولىقى
from bidi.algorithm import get_display
#بىدى ئالگورىزىمى، ئوڭدىن سڭلغا يېزىلىدىغان يېزىقلار ئۈچۈن ئىنتايىن مۇھېمدۇر
import arabic_reshaper
#ئوڭدىن سولغا يېزىلدىغان يېزىقنى شەكىللەندۈرۈش
path_txt='a.txt'
#تېكسىت ھۆججەت نام ۋە يولى
f = open(path_txt,'r',encoding='UTF-8').read()
#تېكسىت ھۆججىتىنى ئېچىش
reshaped_text = arabic_reshaper.reshape(f)
f = get_display(reshaped_text)
#تېكسىتنى ئايرىپ شەكىللەندۈرۈش
wc= WordCloud(font_path="ALKATIP Elipbe.ttf",background_color="white",width=1000,height=880)
#سۆز بۇلىتى رەسىم كۆزنىكىنىڭ خاسلىقى ،مەسىلەن خەت نۇسخىسى،چوڭ كىچىكلىكى قاتارلىقلار
wc.generate(f)
#سۆز بۇلىتى ھاسىل قىلىش
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
#سۆز بۇلىتى رەسىمىنى سىزىش
```
### Picture رەسىملەر












